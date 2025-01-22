from fastapi import APIRouter, Depends, HTTPException, status, Request
from src.database.connection import get_connection
from mysql.connector import MySQLConnection

from src.models.UpdateMateriales import InMaterial
from src.services.querymateriales import Querys_materiales

import re
from datetime import datetime

import json

router = APIRouter(tags=["materiales"])

@router.get("/")
def getS_items(db: MySQLConnection = Depends(get_connection)):
    print("api/materiales")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_materiales.QUERY_MATERIALES
        cursor.execute(query)
        lst_materiales = cursor.fetchall()
        
        return lst_materiales
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()

@router.get("/get_item/{id}")
def get_item(id: str, db: MySQLConnection = Depends(get_connection)):
    print("api/get_items")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_materiales.QUERY_MATERIALES
        query = query + " WHERE ID_cmaterial = " + id + ";"

        cursor.execute(query)
        equipo = cursor.fetchall()
        cursor.close()
        if not equipo:
            raise HTTPException(status_code=404, detail="Item not found")
        return equipo
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()

@router.get("/pendientes")
def get_pendientes(db: MySQLConnection = Depends(get_connection)):
    print("api/materiales/pendientes")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_materiales.QUERY_MATERIALES
        query = query + " WHERE DIFERENCIA != 0"
        cursor.execute(query)
        equipos_pend = cursor.fetchall()
        
        cursor.close()
        if not equipos_pend:
            raise HTTPException(status_code=404, detail="Item not found")
        return equipos_pend
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()

@router.get("/entregados")
def get_entregados(db: MySQLConnection = Depends(get_connection)):
    print("api/materiales/entregados")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_materiales.QUERY_MATERIALES
        query = query + " WHERE DIFERENCIA = 0"
        cursor.execute(query)
        equipos_comp = cursor.fetchall()

        cursor.close()
        if not equipos_comp:
            raise HTTPException(status_code=404, detail="Item not found")
        return equipos_comp
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()

@router.put("/update_material/{id}")
def update_material(id: str, material: InMaterial, db: MySQLConnection = Depends(get_connection) ):
    print("api/materiales/update_material")
    
    try:
        print(material)
        fecha_original = material.Fecha_llegada
        print(fecha_original)

        # Usar una expresión regular para extraer la fecha
        # fecha_extraida = re.match(r"^(.*GMT[+\-]\d{4})", fecha_original).group(1)
        fecha_extraida = re.match(r"^(.*GMT[+\-]\d{4})", fecha_original).group(1)
        print(fecha_extraida)

        # Definir el formato de entrada para analizar la fecha (sin la parte extra)
        formato_entrada = "%a %b %d %Y %H:%M:%S GMT%z"
        print(formato_entrada)

        # Convertir la cadena extraída a un objeto datetime
        fecha_objeto = datetime.strptime(fecha_extraida, formato_entrada)
        print(fecha_objeto)

        # Formatear la fecha al formato "DD-MM-YYYY"
        fecha_formateada = fecha_objeto.strftime("%d-%m-%Y")

        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
            UPDATE railway.control_perneria
            SET 
                TIPO_ELEMENTO = %s,
                TUNEL= %s,
                DISPOSICION_FINAL = %s,
                CANTIDAD_TERRENO = %s,
                DIFERENCIA = %s,
                PROVEEDOR = %s,
                PATIO = %s,
                FECHA_LLEGADA = %s,
                OBSERVACION= %s
            WHERE ID_cmaterial = %s
            """)
        values = (material.Tipo_Elemento, material.Tunel, material.Disposicion_Final, material.Cantidad_Terreno, material.Diferencia, material.Proveedor, material.Patio, fecha_formateada, material.Observacion, int(id))

        print(fecha_formateada)
                                    
        rc = cursor.execute(queryUpdate, values)

        cursor.close()
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"status_code": 200, "message": "Material updated successfully"}
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        
        db.close()
