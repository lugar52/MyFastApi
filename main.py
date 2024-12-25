from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.equipos import router as equipos
from config import Config

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(equipos)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application"}