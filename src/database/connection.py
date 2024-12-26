
import os
import mysql.connector
from mysql.connector import MySQLConnection


def get_connection() -> MySQLConnection:
    return mysql.connector.connect(
        host=os.getenv('MySQL.MYSQLHOST'),
        user=os.getenv('MySQL.MYSQLUSER'),
        password=os.getenv('MySQL.MYSQLPASSWORD'),
        database=os.getenv('MySQL.MYSQLDATABASE'),
        port=os.getenv('MySQL.MYSQLPORT',3306),
    )


""" host=os.getenv('MYSQL_HOST'),
user=os.getenv('MYSQL_USER'),
password=os.getenv('MYSQL_PASS'),
database=os.getenv('MYSQL_DB'),
port=os.getenv('MYSQL_PORT',3306), """

