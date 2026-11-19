from pydantic import BaseModel


class VentaRegistro(BaseModel):
    mes: str
    ventas: float
    clientes: int


class EstadisticasResponse(BaseModel):
    total_ventas: float
    promedio_ventas: float
    total_clientes: int
    mejor_mes: str
