import mysql.connector
import os

# Get environment variables with default values if not set
# db_name = os.getenv('DB_NAME')
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')
db_name = 'baoiam'
db_user = 'baoiam'
db_password = 'Baoiam$123456'
db_host = '3.109.215.128'
db_port = '3306'

# Check if essential environment variables are set
if not all([db_name, db_user, db_password, db_host, db_port]):
    raise ValueError("One or more environment variables are missing")

# Convert port to integer
try:
    db_port = int(db_port)
except ValueError:
    raise ValueError("DB_PORT must be an integer")

# Initialize the connection variable
connection = None

try:
    # Connect to the database
    connection = mysql.connector.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    print("Database connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed")
