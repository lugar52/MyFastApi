from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class InPernos(BaseModel):
    Tunel: int
    Disposicion_Final: int
    Cantidad_Terreno: int
    Diferencia: int
    Patio: int
    Fecha_llegada: str
    Observacion: str
    Stock: int
    SubPatio: int
    Coordenada: int
