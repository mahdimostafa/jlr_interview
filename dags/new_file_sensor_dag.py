from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
    'owner': 'you',
    'start_date': datetime(2023, 9, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def decide_which_path():
    if os.path.exists(file_path):
        return "trigger_main_dag"
    else:
        return "end"

with DAG('file_sensor_dag',
         default_args=default_args,
         schedule_interval='@daily',  # Or '0 0 * * *'
         catchup=False) as dag:

    file_path = '/opt/airflow/plugins/WordbankEconomicData_Trimmed_v2.xlsx'

    sensing_task = FileSensor(
        task_id='sense_file',
        filepath=file_path,
        timeout=60,           # Only wait for 1 minute
        poke_interval=10,     # Check every 10 seconds
        mode='poke',
        soft_fail=True        # Set to True if you want Airflow to continue if the sensor times out
    )

    branch = BranchPythonOperator(
        task_id='branch_task',
        python_callable=decide_which_path
    )

    trigger_main_dag = TriggerDagRunOperator(
        task_id="trigger_main_dag",
        trigger_dag_id="ingest_xl_to_postgres",  # name of the main DAG
        conf={"file_path": file_path}
    )

    end = DummyOperator(
        task_id='end'
    )

    sensing_task >> branch >> [trigger_main_dag, end]
