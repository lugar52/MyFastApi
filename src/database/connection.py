
import os
import mysql.connector
from mysql.connector import MySQLConnection


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'root'),
        database=os.getenv('MYSQL_DATABASE', 'AMSA'),
        port=os.getenv('MYSQL_PORT', '3306'),
    )

