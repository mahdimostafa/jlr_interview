import psycopg2

# Connection parameters - adjust these to your setup
params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'host.docker.internal',   # if Docker is running locally, this might be 'localhost'
    'port': '5432'        # default port for PostgreSQL
}

conn= None 

try:
    conn = psycopg2.connect(**params)
    print("Connected to the PostgreSQL database successfully!")
except Exception as e:
    print(f"Failed to connect to the PostgreSQL database: {e}")
finally:
    if conn:
        conn.close()
