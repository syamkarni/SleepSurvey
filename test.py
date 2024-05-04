import psycopg2

# Database connection parameters
user = 'postgres.xgvolyyoyrcqlldyleds'
password = 'Sleep6369246071'
host = 'aws-0-ap-southeast-1.pooler.supabase.com'
port = '5432'
dbname = 'postgres'

# Connection string
connection_string = f"dbname='{dbname}' user='{user}' host='{host}' port='{port}' password='{password}'"

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(connection_string)
    print("Connection established!")
    # Your database operations go here
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
