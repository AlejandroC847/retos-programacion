""" Módulo encargado de contar la diferencia de dias entre dos fechas diferentes.
Considera la cantidad de dias en cada mes y la existencia de años bisiestos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/14"

import sys
import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def cuantos_dias(f1: str, f2: str) -> int:
    """Calcula la cantidad de días en un rango de fechas definidas.

    Realiza el conteo desde el 01/01/1582, a partir de ahi cuenta la diferencia en dias
    para cada fecha, y resta los valores de cada una entre si, y obteniendo su valor absoluto,
    por lo que el rango no distingue cual es menor o mayor, siempre mostrara la diferencia.

    Args:
        f1 (str): Primer fecha del rango.
        f2 (str): Segunda fecha del rango.

    Raises:
        TypeError: Si los argumentos no son cadenas de texto.
        ValueError: Si la validación de fechas no se cumple exitosamente.

    Returns:
        int: Cantidad de días entre la fecha 1 y la fecha 2.
    """

    if not isinstance(f1, str) or not isinstance(f2, str):
        raise TypeError("Se requieren cadenas de texto como argumentos.")

    if not validar_fecha(f1):
        raise ValueError(
                f"La primer fecha '{f1}' no es válida!.\n"
                "El formato debe ser 'dd/mm/aaaa'. La fecha debe ser real entre 1582 y 9999."
            )
    if not validar_fecha(f2):
        raise ValueError(
                f"La segunda fecha '{f2}' no es válida!.\n"
                "El formato debe ser 'dd/mm/aaaa'. La fecha debe ser real entre 1582 y 9999."
            )

    fecha_inicial = {"dia": 1, "mes": 1, "anio": 1582}
    dias_fecha_1 = 0
    dias_fecha_2 = 0

    #Contar fecha 1
    fecha = f1.split("/")
    dia, mes, anio = map(int, fecha)
    days_in_months  = [31, 29 if is_leap_year(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(fecha_inicial["anio"], anio):
        dias_fecha_1 += 366 if is_leap_year(i) else 365
    for i in range(fecha_inicial["mes"], mes):
        dias_fecha_1 += days_in_months[i - 1]
    dias_fecha_1 += dia - fecha_inicial["dia"]

    #Contar fecha 2
    fecha = f2.split("/")
    dia, mes, anio = map(int, fecha)
    days_in_months  = [31, 29 if is_leap_year(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(fecha_inicial["anio"], anio):
        dias_fecha_2 += 366 if is_leap_year(i) else 365
    for i in range(fecha_inicial["mes"], mes):
        dias_fecha_2 += days_in_months[i - 1]

    dias_fecha_2 += dia - fecha_inicial["dia"]

    return abs(dias_fecha_2 - dias_fecha_1)

def validar_fecha(fecha: str) -> bool:
    """Verifica si una fecha es valida siguiendo el formato establecido "dd/mm/aaaa".

    Args:
        fecha (str): Fecha en cadena de texto a evaluar.

    Returns:
        bool: Resultado de evaluación. Validez exitosa o fracaso.
    """

    #Solo cadenas
    if not isinstance(fecha, str):
        return False

    # 10 caracteres: "dd/mm/aaaa"
    if len(fecha) != 10:
        return False

    #Barras en el lugar adecuado
    if fecha[2] != "/" or fecha[5] != "/":
        return False

    fecha = fecha.split("/") # De string a lista de strings: ['dd', 'mm', 'aaaa']

    # Solo numeros como fecha
    for f in fecha:
        if not f.isdigit():
            return False

    # Convertir a enteros
    dia, mes, anio = map(int, fecha)

    # El año debe ser correcto
    if anio < 1582 or anio > 9999: # No puede ser mayor a 9999 por la cantidad de digitos
    #Desde 1582 (Inicio de calendario Gregoriano) hasta 9999
        return False

    # El mes debe ser correcto
    if mes < 1 or mes > 12:
        return False

    days_in_months  = [31, 29 if is_leap_year(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # El dia debe ser correcto
    if dia < 1 or dia > days_in_months[mes - 1]:
        return False

    return True

def is_leap_year(year: int) -> bool:
    """Determina si un año es bisiesto.

    Args:
        year (int): Año a evaluar si es bisiesto o no.

    Returns:
        bool: Resultado de la evaluación.
    """
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Se requiere un entero como argumento.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def _main():
    """Demo del programa. Ejecución principal"""

    _clear_console()

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Se esperaban exactamente dos fechas!")
        _enter_to_continue()
        return

    print("-" * 20)
    print("Cuántos Días?")
    print("-" * 20)

    if len(sys.argv) == 3:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    else:
        try:
            f1 = input("Ingresa la fecha 1 (dd/mm/aaaa): ")
            f2 = input("Ingresa la fecha 2 (dd/mm/aaaa): ")
        except KeyboardInterrupt:
            print("\nPrograma cancelado por el usuario.")
            return

    try:
        print(
                f"Entre la fecha '{f1}' y la fecha '{f2}' "
                f"hay {cuantos_dias(f1, f2)} días de diferencia.\n"
            )
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    finally:
        input("Presiona Enter para continuar...")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    #_main()

    #DATES = ("01/01/1582", "01/01/1585")  # Esperado: 1096

    # El límite inferior exacto (Primer día del calendario Gregoriano)
    DATES = ("01/01/1582", "02/01/1582")  # Esperado: 1

    # El fin de los tiempos en tu código (Año 9999)
    #DATES = ("30/12/9999", "31/12/9999")  # Esperado: 1

    DIFFERENCE = cuantos_dias(*DATES)

    print(f"Entre la fecha '{DATES[0]}' y '{DATES[1]}' hay {DIFFERENCE} dias de diferencia.")
