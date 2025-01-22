from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class InMaterial(BaseModel):
    Tipo_Elemento: int
    Tunel: int
    Disposicion_Final: int
    Cantidad_Terreno: int
    Diferencia: int
    Proveedor: int
    Patio: int
    Fecha_llegada: str
    Observacion: str