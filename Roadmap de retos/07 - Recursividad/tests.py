"""Módulo para realizar las pruebas unitarias del módulo recursividad.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/20"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import recursividad as r

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_factorial():
    """Verifica el funcionamiento del cálculo de factorial"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para 'factorial()'...")

    assert r.factorial() == 1
    assert r.factorial(0) == 1
    assert r.factorial(5) == 120
    assert r.factorial(10) == 3628800

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Cálculos de factoriales esperados.")

def test_fibonacci():
    """Verifica el funcionamiento del cálculo de la serie fibonacci"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'fibonacci()'...")

    assert r.fibonacci() == 0
    assert r.fibonacci(1) == 0
    assert r.fibonacci(5) == 3
    assert r.fibonacci(332) == 668996615388005031531000081241745415306766517246774551964595292186469

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de cálculos de la posición en fibonacci esperados...")

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError)
    o valores inválidos (ValueError).
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    invalid_integer_type_cases = (True, 9.81, [1, 2], {"tiempo": 2}, None, "8", (4, 5))

    for case in invalid_integer_type_cases:
        with raises(TypeError):
            r.recursivity(case)
            r.factorial(case)
            r.fibonacci(case)

    with raises(ValueError):
        r.factorial(-5)
    with raises(ValueError):
        r.fibonacci(-5)
        r.fibonacci(0)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_factorial()
        test_fibonacci()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
