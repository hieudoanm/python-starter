"""
PostgreSQL
"""


from dotenv import load_dotenv
import os
import psycopg2



load_dotenv()


def get_connection():
    """
    Get Connection
    """
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    database = os.environ.get("DB_NAME")
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    print(host, port, database, user, password)
    return psycopg2.connect(host=host,
                            port=port,
                            database=database,
                            user=user,
                            password=password)
