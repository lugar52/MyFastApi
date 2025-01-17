from fastapi import Depends
from src.database.connection import get_connection
from mysql.connector import MySQLConnection

from src.models.UpdatePernos  import InPernos

class Pernos_Service:

    def update_pernos(Pernos: InPernos, id: str ):
        try:
            db: MySQLConnection = Depends(get_connection)

            # Consulta parametrizada
            queryUpdate = ("""
                UPDATE railway.control_perneria
                SET 
                    TIPO_ELEMENTO = :Tipo_Elemento, 
                    TUNEL= :Tunel, 
                    DISPOSICION_FINAL = :Disposición_Final, 
                    CANTIDAD_TERRENO = :Cantidad_Terreno, 
                    DIFERENCIA = :Diferencia, 
                    PROVEEDOR = :Proveedor, 
                    PATIO = :Patio, 
                    FECHA_LLEGADA = :Fecha_llegada  
                    OBSERVACION= Observacion
                WHERE ID_PERNO = :fila
                """)
            
            parametros = {
                "Cantidad_Terreno": Pernos.Cantidad_Terreno,
                "Tipo_Elemento": Pernos.Tipo_Elemento,
                "Tunel": Pernos.Tunel,
                "Disposicion_Final": Pernos.Disposicion_Final,
                "Proveedor": Pernos.Proveedor,
                "Patio": Pernos.Patio,
                "Diferencia": Pernos.Diferencia,
                "Fecha_llegada": Pernos.Fecha_llegada,
                "Observacion": Pernos.Observacion,
                "fila": int(id),
            }

            cursor = db.cursor(dictionary=True)
            cursor.execute(queryUpdate)
            pernos_comp = cursor.fetchall()

            cursor.close()
        
            # Ejecutar la consulta con parámetros
            return {"rc": 200}
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return {"rc": e}
        finally:
            db.close()