"""Proporciona una función para convertir unidades de tiempo (días, horas, minutos y segundos)
a milisegundos, realizando validaciones de tipo de datos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/11"

import os

MS_PER_SEC = 1000
MS_PER_MIN = MS_PER_SEC * 60
MS_PER_HOUR = MS_PER_MIN * 60
MS_PER_DAY = MS_PER_HOUR * 24

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def convert_time(days: int = 0, hours: int = 0, mins: int = 0, secs: int = 0) -> int:
    """Convierte una cantidad de tiempo dada en días, horas, minutos y segundos a milisegundos.

    Args:
        days (int): Número de días. Por defecto 0.
        hours (int): Número de horas. Por defecto 0.
        mins (int): Número de minutos. Por defecto 0.
        secs (int): Número de segundos. Por defecto 0.

    Returns:
        int: El equivalente del tiempo total expresado en milisegundos.

    Raises:
        TypeError: Si alguno de los argumentos no es de tipo entero.
        """

    # region Validaciones de tipo
    if not isinstance(days, int) or isinstance(days, bool):
        raise TypeError(f"El argumento 'days' debe ser int. Se recibió {type(days).__name__}")

    if not isinstance(hours, int) or isinstance(hours, bool):
        raise TypeError(f"El argumento 'hours' debe ser int. Se recibió {type(hours).__name__}")

    if not isinstance(mins, int) or isinstance(mins, bool):
        raise TypeError(f"El argumento 'mins' debe ser int. Se recibió {type(mins).__name__}")

    if not isinstance(secs, int) or isinstance(secs, bool):
        raise TypeError(f"El argumento 'secs' debe ser int. Se recibió {type(secs).__name__}")
    # endregion

    total_ms = (
        (secs * MS_PER_SEC) +
        (mins * MS_PER_MIN) +
        (hours * MS_PER_HOUR) +
        (days * MS_PER_DAY)
    )

    return total_ms

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Conversor Tiempo")
    print("-" * 20)

    try:
        dias = 2
        horas = 16
        minutos = 25
        segundos = 47
        print(
            f"En {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos hay "
            f"{convert_time(dias, horas, minutos, segundos)} milisegundos.\n"
        )

    except TypeError as te:
        print(te)
    finally:
        input("Presiona Enter para continuar...")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
