from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from create_tables_psql import create_tables

# Default arguments for your DAG
default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define your DAG
dag = DAG(
    'create_tables_dag',
    default_args=default_args,
    description='A DAG to create Postgres tables if they do not exist',
    # schedule_interval=timedelta(days=1),
    schedule_interval=None,
)

# Define your PythonOperator task
create_tables_task = PythonOperator(
    task_id='create_tables',
    python_callable=create_tables,
    dag=dag,
)

# Set the task execution order (if you have more tasks in the future)
create_tables_task
