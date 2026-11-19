# Dashboard de Ventas - API con FastAPI

Aplicación web y API REST desarrollada en **Python** con **FastAPI** para visualizar y analizar métricas de ventas y crecimiento de clientes a partir de un dataset CSV.

## Estructura del Proyecto

El código está organizado bajo una arquitectura modular separada por responsabilidades:

```text
dashboard_ventas/
├── BDD/
│   ├── __init__.py
│   └── conexion.py          # Gestión del archivo ventas.csv y carga inicial de datos
├── models/
│   ├── __init__.py
│   └── venta_model.py       # Esquemas Pydantic para validación de datos y respuestas
├── controllers/
│   ├── __init__.py
│   └── venta_controller.py  # Lógica de negocio, estadísticas, gráficos y plantilla HTML
├── routes/
│   ├── __init__.py
│   └── venta_routes.py      # Definición de rutas (endpoints GET)
├── main.py                  # Punto de entrada principal de la aplicación FastAPI
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación general
└── CHANGELOG.md             # Historial de cambios y versiones
```

## Requisitos e Instalación

1. Asegúrate de tener **Python 3.10+** instalado.
2. Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

Inicia el servidor local desde la carpeta raíz del proyecto:

```bash
uvicorn main:app --reload
```

Luego abre tu navegador en:
* **Dashboard Web:** `http://127.0.0.1:8000/`
* **Documentación interactiva (Swagger UI):** `http://127.0.0.1:8000/docs`

## Endpoints Disponibles

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| `GET` | `/` | Interfaz web principal con indicadores y gráficos |
| `GET` | `/datos` | Devuelve los registros del dataset en formato JSON |
| `GET` | `/estadisticas` | Retorna el total de ventas, promedio, total de clientes y mejor mes |
| `GET` | `/grafico/barras` | Genera y devuelve la imagen PNG del gráfico de ventas mensuales |
| `GET` | `/grafico/lineas` | Genera y devuelve la imagen PNG del gráfico de crecimiento de clientes |
