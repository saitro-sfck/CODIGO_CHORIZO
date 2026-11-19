# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

## [1.0.0] - 2026-11-18

### Agregado
- **Arquitectura modular:** Separación del código monolítico original en paquetes independientes (`BDD`, `models`, `controllers`, `routes`).
- **Capa de datos (`BDD/conexion.py`):** Creación automática y lectura segura de `ventas.csv` usando `pathlib` y `pandas`.
- **Modelos de validación (`models/venta_model.py`):** Esquemas `VentaRegistro` y `EstadisticasResponse` con Pydantic.
- **Controladores (`controllers/venta_controller.py`):** Lógica desacoplada para cálculos estadísticos, generación de gráficos en memoria con Matplotlib y renderizado del dashboard HTML.
- **Rutas (`routes/venta_routes.py`):** Implementación de `APIRouter` para gestionar todos los endpoints `GET`.
- **Documentación y dependencias:** Inclusión de `README.md`, `CHANGELOG.md` y `requirements.txt`.

### Corregido
- Corrección de sintaxis en la ruta de archivo (`__file__` en lugar de `_file_`) para evitar errores de ejecución en Python.
