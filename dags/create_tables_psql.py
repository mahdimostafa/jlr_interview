import psycopg2

# Database configuration - update these as necessary
DATABASE_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'host.docker.internal',   # if Docker is running locally, this might be 'localhost'
    'port': '5432'        # default port for PostgreSQL
}

COUNTRY_DATA_SCHEMA = {
    "Country Or Region Name": "VARCHAR",
    "Country Code": "VARCHAR",
    "Currency Unit": "VARCHAR",
    "Country Region": "VARCHAR",
    "Country Income Group": "VARCHAR",
    "Topic": "VARCHAR",
    "Indicator Name": "VARCHAR",
    "2000": "FLOAT",
    "2001": "FLOAT",
    "2002": "FLOAT",
    "2003": "FLOAT",
    "2004": "FLOAT",
    "2005": "FLOAT",
    "2006": "FLOAT",
    "2007": "FLOAT",
    "2008": "FLOAT",
    "2009": "FLOAT",
    "2010": "FLOAT",
    "2011": "FLOAT",
    "2012": "FLOAT",
    "2013": "FLOAT",
    "2014": "FLOAT",
    "2015": "FLOAT",
    "2016": "FLOAT",
    "2017": "FLOAT",
    "2018": "FLOAT",
    "2019": "FLOAT",
    "2020": "FLOAT",
    "ingestion_timestamp": "TIMESTAMP"
}

TOPICS_SCHEMA = {
    "Topic": "VARCHAR",
    "Topic_1": "VARCHAR",
    "Indicator Name": "VARCHAR",
    "ingestion_timestamp": "TIMESTAMP"
}

INGESTED_FILES_SCHEMA = {
    "file_name": "VARCHAR",
    "ingested_timestamp": "TIMESTAMP"
}

def create_table_if_not_exists(table_name, schema):
    # Create a connection
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name=%s)", (table_name,))
    if not cursor.fetchone()[0]:
        create_stmt = f"""
        CREATE TABLE {table_name} (
            {', '.join([f'"{col}" {col_type}' for col, col_type in schema.items()])}
        );
        """
        cursor.execute(create_stmt)
        conn.commit()

    cursor.close()
    conn.close()

# Run the function for each table
def create_tables():
    create_table_if_not_exists('country_data', COUNTRY_DATA_SCHEMA)
    create_table_if_not_exists('topics', TOPICS_SCHEMA)
    create_table_if_not_exists('ingested_files', INGESTED_FILES_SCHEMA)
