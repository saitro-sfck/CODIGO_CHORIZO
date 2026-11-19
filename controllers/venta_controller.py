from io import BytesIO
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from BDD.conexion import obtener_conexion_df
from models.venta_model import VentaRegistro, EstadisticasResponse


def listar_datos() -> list[VentaRegistro]:
    df = obtener_conexion_df()
    registros = df.to_dict(orient="records")
    # Validamos cada fila usando el modelo
    return [VentaRegistro(**fila) for fila in registros]


def calcular_estadisticas() -> EstadisticasResponse:
    df = obtener_conexion_df()
    return EstadisticasResponse(
        total_ventas=float(df["ventas"].sum()),
        promedio_ventas=float(df["ventas"].mean()),
        total_clientes=int(df["clientes"].sum()),
        mejor_mes=str(df.loc[df["ventas"].idxmax(), "mes"])
    )


def generar_grafico(tipo: str) -> bytes:
    df = obtener_conexion_df()
    fig, ax = plt.subplots(figsize=(9, 4))

    if tipo == "barras":
        ax.bar(df["mes"], df["ventas"], color="royalblue")
        ax.set_title("Ventas por mes")
        ax.set_ylabel("Ventas ($)")
    else:
        ax.plot(df["mes"], df["clientes"], marker="o", color="green", linewidth=3)
        ax.set_title("Crecimiento de clientes")
        ax.set_ylabel("Clientes")

    ax.grid(axis="y", alpha=0.2)
    plt.xticks(rotation=25)
    plt.tight_layout()

    imagen = BytesIO()
    fig.savefig(imagen, format="png", dpi=120)
    plt.close(fig)

    return imagen.getvalue()


def construir_html_dashboard() -> str:
    stats = calcular_estadisticas()

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Dashboard de Ventas</title>
        <style>
            body {{
                font-family: Arial;
                background: #f0f4f8;
                padding: 30px;
            }}
            h1 {{
                color: #1e3a5f;
            }}
            .indicadores {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }}
            .tarjeta {{
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 8px #ddd;
                flex: 1;
                min-width: 160px;
            }}
            .graficos {{
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 25px;
            }}
            .graficos img {{
                width: 100%;
                max-width: 580px;
                border-radius: 10px;
                background: white;
            }}
        </style>
    </head>
    <body>
        <h1>Dashboard de Ventas</h1>
        <p>Análisis de datos con Python y FastAPI</p>

        <div class="indicadores">
            <div class="tarjeta">
                <h3>Ventas totales</h3>
                <h2>${stats.total_ventas:,.2f}</h2>
            </div>
            <div class="tarjeta">
                <h3>Promedio mensual</h3>
                <h2>${stats.promedio_ventas:,.2f}</h2>
            </div>
            <div class="tarjeta">
                <h3>Clientes registrados</h3>
                <h2>{stats.total_clientes}</h2>
            </div>
        </div>

        <div class="graficos">
            <img src="/grafico/barras">
            <img src="/grafico/lineas">
        </div>

        <p>
            <a href="/datos">Ver Dataset</a> |
            <a href="/estadisticas">Ver estadísticas</a> |
            <a href="/docs">Documentación API</a>
        </p>
    </body>
    </html>
    """
