import mysql.connector
import os

def get_db_connection():
    """Establish and return a database connection."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD", "123456"),  # Secure handling
            database="spam_detection"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database connection error: {err}")
        return None
