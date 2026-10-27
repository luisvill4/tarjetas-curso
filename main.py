"""Muestra la tarjeta de cada estudiante que está en la carpeta estudiantes/."""
import importlib.util
from pathlib import Path


def cargar_tarjetas():
    carpeta = Path(__file__).parent / "estudiantes"
    tarjetas = []
    for archivo in sorted(carpeta.glob("*.py")):
        spec = importlib.util.spec_from_file_location(archivo.stem, archivo)
        modulo = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(modulo)
            tarjetas.append((archivo.name, modulo.presentarme()))
        except (Exception, SystemExit) as error:
            tarjetas.append((archivo.name, f"[error en este archivo: {error}]"))
    return tarjetas


if __name__ == "__main__":
    tarjetas = cargar_tarjetas()
    print(f"Tarjetas del curso ({len(tarjetas)})")
    print("-" * 40)
    for archivo, mensaje in tarjetas:
        print(mensaje)
