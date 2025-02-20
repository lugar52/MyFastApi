from fastapi import APIRouter, Depends, HTTPException, status, Request
from src.database.connection import get_connection
from mysql.connector import MySQLConnection

from src.models.UpdatePernos import InPernos

from src.services.queryPerneria import Querys_perneria

import re
from datetime import datetime

import json

router = APIRouter(tags=["perneria"])

@router.get("/")
def getS_items(db: MySQLConnection = Depends(get_connection)):
    print("api/perneria")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        cursor.execute(query)
        lst_equipos = cursor.fetchall()
        
        return lst_equipos
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()

@router.get("/get_item/{id}")
async def get_item(id: str, db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/get_items")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        query = query + " WHERE ID_PERNO = " + id + ";"

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

@router.get("/todos")
def get_todos(db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/todos")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        
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

@router.get("/pendientes")
def get_pendientes(db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/pendientes")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        query = query + " WHERE DIFERENCIA < 0"
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

@router.get("/entregada")
def get_entregados(db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/entregada")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        query = query + " WHERE DIFERENCIA >= 0"
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

@router.put("/update_perno/{id}")
def update_perno(id: str, perno: InPernos, db: MySQLConnection = Depends(get_connection) ):
    print("api/perneria/update_perno")
    
    try:
        print(perno)
        fecha_original = perno.Fecha_llegada
        print(fecha_original)

        # Usar una expresión regular para extraer la fecha
        # fecha_extraida = re.match(r"^(.*GMT[+\-]\d{4})", fecha_original).group(1)
        # fecha_extraida = re.match(r"^(.*GMT[+\-]\d{4})", fecha_original).group(1)
        

        # Definir el formato de entrada para analizar la fecha (sin la parte extra)
        # formato_entrada = "%a %b %d %Y %H:%M:%S GMT%z"
        # print(formato_entrada)

        # Convertir la cadena extraída a un objeto datetime
        # fecha_objeto = datetime.strptime(fecha_extraida, formato_entrada)
        # print(fecha_objeto)

        # Formatear la fecha al formato "DD-MM-YYYY"
        # fecha_formateada = fecha_objeto.strftime("%d-%m-%Y")

        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
            UPDATE railway.control_perneria
            SET 
                TUNEL= %s,
                DISPOSICION_FINAL = %s,
                CANTIDAD_TERRENO = %s,
                DIFERENCIA = %s,
                PATIO = %s,
                FECHA_LLEGADA = %s,
                OBSERVACION= %s,
                STOCK= %s,
                SUB_PATIO= %s,
                COORDENADAS= %s
            WHERE ID_PERNO = %s
            """)
        values = (perno.Tunel, perno.Disposicion_Final, perno.Cantidad_Terreno, perno.Diferencia, perno.Patio, fecha_original, perno.Observacion, perno.Stock, perno.SubPatio, perno.Coordenada, int(id))

        rc = cursor.execute(queryUpdate, values)

        cursor.close()
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"status_code": 200, "message": "Item updated successfully"}
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        db.close()

@router.get("/proveedores")
def get_entregados(db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/proveedores")
    try:
        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
                select p.ID_PROVEEDOR, p.DESCRIPCION from proveedor p
                """)
        
        cursor.execute(queryUpdate)
        ls_proveedores = cursor.fetchall()
        print(ls_proveedores)

        cursor.close()
        if not ls_proveedores:
            raise HTTPException(status_code=404, detail="Item not found")
        return ls_proveedores
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        db.close()

@router.get("/proveedor/{id}")
def get_proveedor(id: str, db: MySQLConnection = Depends(get_connection)):
    print("api/perneria/proveedor")
    try:
        cursor = db.cursor(dictionary=True)
        query = Querys_perneria.QUERY_PERNERIA
        query = query + " WHERE PROVEEDOR = %s"
        values = (id,)

        cursor.execute(query, values)
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

@router.get("/materiales/{prov}/{cond}")
async def get_Despachos(prov: str, cond: str, db: MySQLConnection = Depends(get_connection)):
    print("materiales")
    print(prov)
    print(cond)

    try:
        cursor = db.cursor(dictionary=True)
        query = ("""
            CALL PROC_QUERY_PERNERIA(%s, %s);
            """)
        values = (prov, cond,)
        despachos = cursor.execute(query, values)
        despachos = cursor.fetchall()
        
        if not despachos:
            raise HTTPException(status_code=404, detail="Item not found")
        return despachos
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        cursor.close()
        db.close()        