from pathlib import Path
import pandas as pd

# Apuntamos a la raíz del proyecto para que ventas.csv se guarde junto a main.py
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_CSV = BASE_DIR / "ventas.csv"


def inicializar_bdd():
    """Crea el archivo CSV con datos iniciales si aún no existe."""
    if not ARCHIVO_CSV.exists():
        datos = {
            "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
            "ventas": [1200, 1800, 1500, 2300, 2800, 3500],
            "clientes": [25, 32, 29, 40, 46, 58]
        }
        df = pd.DataFrame(datos)
        df.to_csv(ARCHIVO_CSV, index=False)


def obtener_conexion_df() -> pd.DataFrame:
    """Asegura que exista la BDD y devuelve el DataFrame leído."""
    inicializar_bdd()
    return pd.read_csv(ARCHIVO_CSV)
