from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Trilli(BaseModel):
    nombre: str
    rut: str
    talla: str 
    carrera: Optional[str]

@app.get("/")
def index():
    return {"message" :"Hola Trillizos"}

@app.get("/trillizos/{id}")
def mostrar_trillizo(id: int):
    if id == 1:
        return {"Nombre" : "Vicente"}
    if id == 2:
        return {"Nombre" : "Gaspar"}
    else:
        return {"Nombre" : "Matilde"}

@app.post("/trilli")
def insertar_trilli(trilli: Trilli):
    return {"message": f"{trilli.nombre} ingresado"}
