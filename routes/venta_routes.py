from fastapi import APIRouter
from fastapi.responses import HTMLResponse, Response

from models.venta_model import VentaRegistro, EstadisticasResponse
from controllers import venta_controller

router = APIRouter()


@router.get("/datos", response_model=list[VentaRegistro])
def obtener_datos_endpoint():
    return venta_controller.listar_datos()


@router.get("/estadisticas", response_model=EstadisticasResponse)
def obtener_estadisticas_endpoint():
    return venta_controller.calcular_estadisticas()


@router.get("/grafico/barras")
def obtener_grafico_barras():
    imagen = venta_controller.generar_grafico("barras")
    return Response(content=imagen, media_type="image/png")


@router.get("/grafico/lineas")
def obtener_grafico_lineas():
    imagen = venta_controller.generar_grafico("lineas")
    return Response(content=imagen, media_type="image/png")


@router.get("/", response_class=HTMLResponse)
def mostrar_dashboard():
    html = venta_controller.construir_html_dashboard()
    return HTMLResponse(content=html)
