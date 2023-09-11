from datetime import datetime, timedelta
import shutil, os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from ingest_data_to_psql import ingest_excel

def archive_file(file_path, processed_dir='processed_files'):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist!")

    # Create processed directory if it doesn't exist
    os.makedirs(processed_dir, exist_ok=True)

    ingest_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    new_file_name = f"{os.path.basename(file_path)}_ingested_{ingest_timestamp}.xlsx"
    new_file_path = os.path.join(processed_dir, new_file_name)

    # Use shutil.copy2 to keep metadata, then remove the original file
    shutil.copy2(file_path, new_file_path)
    os.remove(file_path)

    return f"File {file_path} has been moved to {new_file_path}"



default_args = {
    'owner': 'you',
    'start_date': datetime(2023, 9, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('ingest_xl_to_postgres',
         default_args=default_args,
         schedule_interval=None,  # We don't set a schedule as it's triggered by the sensor DAG
         catchup=False) as dag:

    file_path = "{{ dag_run.conf['file_path'] }}"  # Retrieve file path from configuration

    ingest_task = PythonOperator(
        task_id='ingest_to_postgres',
        python_callable=ingest_excel,
        op_args=[file_path]
    )

    archive_task = PythonOperator(
        task_id='archive_file',
        python_callable=archive_file,
        op_args=[file_path]
    )

    ingest_task >> archive_task
