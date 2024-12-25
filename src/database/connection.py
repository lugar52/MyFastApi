
import os
import mysql.connector
from mysql.connector import MySQLConnection


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASS'),
        database=os.getenv('MYSQL_DB'),
        port=os.getenv('MYSQL_PORT',3306),
    )

