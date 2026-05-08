"""
Módulo para realizar las pruebas del módulo es_un_palindromo.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/07"

import factorial_recursivo as fr
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _limpiar_pantalla():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_factorial_recursivo():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función factorial_recursivo()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'factorial_recursivo()'...")

    assert fr.factorial_recursivo(0) == 1
    assert fr.factorial_recursivo(1) == 1
    assert fr.factorial_recursivo(5) == 120
    assert fr.factorial_recursivo(10) == 3628800

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de cálculo de factoriales esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, "847", True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            fr.factorial_recursivo(caso)

    with raises(ValueError):
        fr.factorial_recursivo(-5)

    with raises(RecursionError):
        fr.factorial_recursivo(5000)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _limpiar_pantalla()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_factorial_recursivo()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
