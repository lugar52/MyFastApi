from fastapi import APIRouter, Depends, HTTPException, status, Request
from src.database.connection import get_connection
from mysql.connector import MySQLConnection

from src.models.UpdatePernos import InPernos
from src.models.despacho import Despacho

from src.services.queryPerneria import Querys_perneria

import re
from datetime import datetime

import json

router = APIRouter(tags=[""])

@router.post("/ingresos")
def despacho(despacho: Despacho, db: MySQLConnection = Depends(get_connection) ):
    print("api/despachos/ingresos")
    
    try:
        print(despacho)

        cursor = db.cursor(dictionary=True)
        queryUpdate = ("""
            call railway.PROC_DESPACHO(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """)
        values = (
            despacho.id_perno,
            despacho.Fecha_despacho,
            despacho.Hora_despacho,
            despacho.Codigo,
            despacho.descricpcion,
            despacho.snf,
            despacho.stock_Inicial,
            despacho.cantidad,
            despacho.stock_final,
            despacho.peso_despacho,
            despacho.lugar_despacho,
            despacho.destino,
            despacho.rut_Retira,
            despacho.Nombre_retira,
            despacho.guia
        )

        print(queryUpdate)
                                   
        rc = cursor.execute(queryUpdate, values)
        print(cursor.rowcount)

        """ cursor.close() """
        """ db.commit() """

        if cursor.rowcount == 0:
            return {"status_code": 200, "message": "Item insert successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        db.rollback()
        return {"status_code": 503, "message": f"Ocurrió un error: {e}"}
    finally:
        db.close()        

@router.get("/get_idpernos/{id}")
async def get_Despachos(id: str, db: MySQLConnection = Depends(get_connection)):
    print()

    try:
        cursor = db.cursor(dictionary=True)
        query = ("""
            CALL PROC_DESPACHOS_X_IDPERNO(%s);
            """)
        values = (id,)
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
