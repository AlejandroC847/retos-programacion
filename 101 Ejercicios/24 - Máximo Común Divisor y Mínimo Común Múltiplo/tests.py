"""Módulo para realizar las pruebas unitarias del módulo mcd_y_mcm.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import mcd_y_mcm as mm

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_mcd():
    """Verifica el funcionamiento del cálculo de MCD"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para 'mcd()'...")

    # Números primos
    assert mm.mcd(13, 7) == 1
    # Múltiplos directos
    assert mm.mcd(20, 5) == 5
    # Mayor primero
    assert mm.mcd(48, 18) == 6
    # Menor primero
    assert mm.mcd(18, 48) == 6
    # Compuestos
    assert mm.mcd(24, 36) == 12
    # 0 primero
    assert mm.mcd(0, 5) == 5
    # 0 segundo
    assert mm.mcd(5, 0) == 5
    # Un argumento negativo
    assert mm.mcd(-12, 18) == 6
    # Ambos negativos
    assert mm.mcd(-9, -15) == 3
    # Número 1
    assert mm.mcd(1, 300) == 1
    # Número iguales
    assert mm.mcd(5, 5) == 5

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Cálculos de MCD esperadas.")

def test_mcm():
    """Verifica el funcionamiento del cálculo de mcm"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para 'mcm()'...")

    # Números primos
    assert mm.mcm(3, 5) == 15
    # Múltiplos directos
    assert mm.mcm(4, 12) == 12
    # Menor primero
    assert mm.mcm(6, 10) == 30
    # Mayor primero
    assert mm.mcm(10, 6) == 30
    # Compuestos
    assert mm.mcm(8, 12) == 24
    # 0 primero
    assert mm.mcm(0, 5) == 0
    # 0 segundo
    assert mm.mcm(7, 0) == 0
    # Ambos son 0
    assert mm.mcm(0, 0) == 0
    # Un argumento negativo
    assert mm.mcm(-4, 6) == 12
    # Ambos negativos
    assert mm.mcm(-9, -12) == 36
    # Número 1
    assert mm.mcm(1, 99) == 99
    # Número iguales
    assert mm.mcm(15, 15) == 15

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Cálculos de mcm esperadas.")

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    invalid_integer_type_cases = (True, 9.81, [1, 2], {"tiempo": 2}, None, "Foo", (4, 5))

    for case in invalid_integer_type_cases:
        with raises(TypeError):
            mm.mcd(case, 1)
            mm.mcm(case, 1)
            mm.mcd(1, case)
            mm.mcm(1, case)

    with raises(ValueError):
        mm.mcd(0, 0)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_mcd()
        test_mcm()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
