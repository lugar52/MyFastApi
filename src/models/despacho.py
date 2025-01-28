from pydantic import BaseModel

class Despacho(BaseModel):
    id_perno: int
    Fecha_despacho: str
    Hora_despacho: str
    Codigo: str
    descricpcion: str
    snf: str
    stock_Inicial: float
    cantidad: float
    stock_final: float
    peso_despacho: float
    lugar_despacho: int
    destino: int
    rut_Retira: str
    Nombre_retira: str
    guia: int


