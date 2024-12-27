
from functools import lru_cache

import mysql.connector
from mysql.connector import MySQLConnection

from fastapi import Depends

from config import Settings

@lru_cache()
def get_settings():
    return Settings()

def get_connection(settings: Settings = Depends(get_settings)) -> MySQLConnection:
    print(settings.MYSQLUSER)
    print(settings.MYSQLPASSWORD)
    print(settings.MYSQLHOST)
    print(settings.MYSQLDATABASE)
    print(settings.MYSQLPORT)
    
    return mysql.connector.connect(
        host=settings.MYSQLHOST,
        user=settings.MYSQLUSER,
        password=settings.MYSQLPASSWORD,
        database=settings.MYSQLDATABASE,
        port=settings.MYSQLPORT,
    )


