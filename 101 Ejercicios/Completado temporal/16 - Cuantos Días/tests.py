"""
Módulo para realizar las pruebas del módulo cuantos_dias.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/06"

import cuantos_dias as cd
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_leap_year():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función is_leap_year()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_leap_year()'...")

    # Son años bisiestos
        # Años simples
    assert cd.is_leap_year(4)
    assert cd.is_leap_year(40)
    assert cd.is_leap_year(2024)
        # Divisible sobre 400
    assert cd.is_leap_year(2000)
        # El año 0 (1 a.C. historicamente)
    assert cd.is_leap_year(0)
        # Algunos negativos como -4 (5 a.C. historicamente)
    assert cd.is_leap_year(-4)

    # No son años bisiestos
        # Años simples
    assert not cd.is_leap_year(1)
    assert not cd.is_leap_year(7)
    assert not cd.is_leap_year(2026)
        # Divisible sobre 100 pero no 400
    assert not cd.is_leap_year(1900)
    assert not cd.is_leap_year(500)
    assert not cd.is_leap_year(100)
    assert not cd.is_leap_year(100)
        # Algunos negativos como -1 (2 a.C. historicamente)
    assert not cd.is_leap_year(-1)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de evaluación de años bisiestos esperados...")

def test_validar_fecha():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función validar_fecha()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'validar_fecha()'...")

    #Formato equivocado
    assert not cd.validar_fecha("6/6/2026") #? Corrección futura para soportarla
    assert not cd.validar_fecha("2026/06/06")
    assert not cd.validar_fecha("dd/mm/aaaa")
    assert not cd.validar_fecha("3./¡1/ñ%$6")
    assert not cd.validar_fecha(6062026)

    #Fechas fuera de limite
        # Año invalido
    assert not cd.validar_fecha("15/05/1221")
    assert not cd.validar_fecha("12/04/10125")
        # Mes invalido
    assert not cd.validar_fecha("06/15/2026")
    assert not cd.validar_fecha("06/00/2026")
        # Día invalido
    assert not cd.validar_fecha("40/06/2026")
    assert not cd.validar_fecha("00/06/2026")
    assert not cd.validar_fecha("29/02/2026") #No es bisiesto

    # Fechas validas
    assert cd.validar_fecha("06/06/2026")
    assert cd.validar_fecha("01/01/1582")
    assert cd.validar_fecha("31/12/9999")
    assert cd.validar_fecha("29/02/2024")


    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de validación de fechas esperados...")

def test_cuantos_dias():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función cuantos_dias()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'cuantos_dias()'...")

    # Pruebas comunes
        # 3 años completos (1584 es bisiesto) -> 1,096 días
    assert cd.cuantos_dias("01/01/1582", "01/01/1585") ==  1096
        # Mismo día y mes, un año común de diferencia -> 365 días
    assert cd.cuantos_dias("15/05/2021", "15/05/2022") ==  365
        # Diferencia de un solo día en meses ordinarios
    assert cd.cuantos_dias("30/04/2023", "01/05/2023") == 1
        # Orden invertido
    assert cd.cuantos_dias("01/12/2025", "25/12/2025") == 24
    assert cd.cuantos_dias("25/12/2025", "01/12/2025") == 24

    #Pruebas con años bisiestos
        # Año bisiesto (2024 fue bisiesto, cruza el 29 de febrero)
    assert cd.cuantos_dias("20/02/2024", "05/03/2024") == 14
        # Año común equivalente (2023 no fue bisiesto, febrero tuvo 28)
    assert cd.cuantos_dias("20/02/2023", "05/03/2023") == 13
        # El año 1900 NO fue bisiesto (múltiplo de 100 pero no de 400)
    assert cd.cuantos_dias("28/02/1900", "01/03/1900") == 1
        # El año 2000 SÍ fue bisiesto (múltiplo de 400)
    assert cd.cuantos_dias("28/02/2000", "01/03/2000") == 2

    # Limites historicos
        # El límite inferior exacto (Primer día del calendario Gregoriano)
    assert cd.cuantos_dias("01/01/1582", "02/01/1582") == 1
        # El limite superior de conteo (Año 9999)
    assert cd.cuantos_dias("30/12/9999", "31/12/9999") == 1

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de cálculo de días esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo_bisiesto = [9.81, "847", True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo_bisiesto:
        with raises(TypeError):
            cd.is_leap_year(caso)

    casos_invalidos_tipo_conteo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]
    for caso_x in casos_invalidos_tipo_conteo:
        for caso_y in casos_invalidos_tipo_conteo:
            with raises(TypeError):
                cd.cuantos_dias(caso_x, caso_y)

    with raises(ValueError):
        cd.cuantos_dias("01/01/0001", "06/06/2026")
        cd.cuantos_dias("06/06/2026", "01/01/0001")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_leap_year()
        test_validar_fecha()
        test_cuantos_dias()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
