from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.perneria import router as perneria
from src.routers.despachos import router as despachos

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(perneria, prefix="/api/perneria" )
app.include_router(despachos, prefix="/api/movimientos" )

@app.get("/api/control_patio")
def read_root():
    return {"message": "Welcome to the Control Patio application BONATTi 2025"}