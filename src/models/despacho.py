from pydantic import BaseModel

class Despacho(BaseModel):
    id_perno: int
    Fecha_despacho: str
    Codigo: int
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
    stock_final: int
    guia: int