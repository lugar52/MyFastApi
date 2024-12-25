from pydantic import BaseModel


class Equipos(BaseModel):
    OC: str
    Contrato: str
    Guía: int
    SNF: str
    Bulto: int
    Itemcode: str
    Tipo_Elemento: str
    Marca: str
    Tunel: str
    Disposición_Final: str
    Cantidad_SNF: int
    Cantidad_Terreno: int
    Diferencia: int
    Peso_Unitario: float
    Peso_Total: float
    Proveedor: str
    Patio: str
    Fecha_llegada: str
    Observación: str
    N_bulto_asig_terreno: int


