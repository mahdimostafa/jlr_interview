import os
import shutil
import pandas as pd
import psycopg2
from datetime import datetime
from psycopg2 import extras

DATABASE_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'host.docker.internal',   # if Docker is running locally, this might be 'localhost'
    'port': '5432'        # default port for PostgreSQL
}

def get_connection():
    return psycopg2.connect(**DATABASE_CONFIG)

def file_already_ingested(file_name, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingested_files WHERE file_name = %s", (file_name,))
    result = cursor.fetchall()
    return len(result) > 0

def insert_data_from_excel(file_path, table_name, conn):
    # Read data from Excel
    data = pd.read_excel(file_path, sheet_name=table_name)
    
    # Convert dataframe to list of tuples
    tuples = [tuple(x) for x in data.to_numpy()]
    
    # Get columns names from dataframe and quote them
    columns = ','.join([f'"{col}"' for col in data.columns])
    
    # Prepare the INSERT query
    query = f"INSERT INTO {table_name} ({columns}) VALUES %s"
    cursor = conn.cursor()
    extras.execute_values(cursor, query, tuples)
    conn.commit()

def record_file_ingestion(file_name, conn):
    now = datetime.now()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ingested_files (file_name, ingested_timestamp) VALUES (%s, %s)", (file_name, now))
    conn.commit()

def ingest_excel(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Skipping ingestion.")
        return

    with get_connection() as conn:
        # Check if the file has been previously ingested
        if file_already_ingested(file_path, conn):
            print(f"File {file_path} has already been ingested. Skipping.")
            return
        
        # Insert data into tables
        insert_data_from_excel(file_path, 'country_data', conn)
        insert_data_from_excel(file_path, 'topics', conn)
        
        # Record the file ingestion
        record_file_ingestion(file_path, conn)
        
        # Optionally, move and rename the ingested file
        # ingest_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        # processed_dir = 'processed_files'
        # if not os.path.exists(processed_dir):
        #     os.makedirs(processed_dir)
        # new_file_path = os.path.join(processed_dir, f"{os.path.basename(file_path)}_ingested_{ingest_timestamp}.xlsx")
        # shutil.move(file_path, new_file_path)
        
        # print(f"File {file_path} has been ingested and moved to {new_file_path}")

# Example usage:
ingest_excel('/opt/airflow/plugins/WordbankEconomicData_Trimmed_v2.xlsx')
