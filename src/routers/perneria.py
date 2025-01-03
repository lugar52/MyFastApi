from fastapi import APIRouter, Depends, HTTPException
from src.database.connection import get_connection
from mysql.connector import MySQLConnection

from src.models.equipos import Equipos
from src.services.queryPerneria import Querys_perneria

router = APIRouter(prefix="/perneria", tags=["perneria"])

@router.get("/")
def getS_items(db: MySQLConnection = Depends(get_connection)):
    cursor = db.cursor(dictionary=True)
    query = Querys_perneria.QUERY_ALL_PERNERIA
    cursor.execute(query)
    lst_equipos = cursor.fetchall()
    cursor.close()
    return lst_equipos

@router.get("/{item_id}")
def get_item(item_id: str, db: MySQLConnection = Depends(get_connection)):
    print("llegue 2")
    cursor = db.cursor(dictionary=True)
    query = Querys_perneria.QUERY_PERNERIA_X_SNF
    query = query + " WHERE SNF = " + item_id + ";"
    cursor.execute(query)
    equipo = cursor.fetchall()
    cursor.close()
    if not equipo:
        raise HTTPException(status_code=404, detail="Item not found")
    return equipo

@router.get("/equipos/pendientes")
def get_item(db: MySQLConnection = Depends(get_connection)):
    print("llegue")
    cursor = db.cursor(dictionary=True)
    query = Querys_perneria.QUERY_PERNERIA_PENDIENTES
    cursor.execute(query)
    equipos_pend = cursor.fetchall()
    cursor.close()
    if not equipos_pend:
        raise HTTPException(status_code=404, detail="Item not found")
    return equipos_pend

@router.get("/equipos/completos")
def get_item(db: MySQLConnection = Depends(get_connection)):
    cursor = db.cursor(dictionary=True)
    query = Querys_perneria.QUERY_PERNERIA_COMPLETAS
    cursor.execute(query)
    equipos_comp = cursor.fetchall()
    cursor.close()
    if not equipos_comp:
        raise HTTPException(status_code=404, detail="Item not found")
    return equipos_comp


