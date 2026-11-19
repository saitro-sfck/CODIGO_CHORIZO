from fastapi import FastAPI
from routes.venta_routes import router as venta_router

app = FastAPI(title="Dashboard de Ventas")

# Conectamos las rutas a la aplicación principal
app.include_router(venta_router)
