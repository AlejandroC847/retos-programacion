"""
Módulo para realizar las pruebas del módulo es_un_numero_de_armstrong.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/09"

import es_un_numero_de_armstrong as arm
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_armstrong():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función is_armstrong()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_armstrong()'...")

    for i in range(10): #Todos los numeros del 0 al 9 son narcisistas (de Armstrong)
        assert arm.is_armstrong(i)

    # Son números narcisistas
    assert arm.is_armstrong(153)
    assert arm.is_armstrong(1634)
    assert arm.is_armstrong(92727)

    # No son números narcisistas
    assert not arm.is_armstrong(10)
    assert not arm.is_armstrong(154)
    assert not arm.is_armstrong(152)
    assert not arm.is_armstrong(500)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de cálculo de números narcisistas esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, "847", True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            arm.is_armstrong(caso)

    with raises(ValueError):
        arm.is_armstrong(-5)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_armstrong()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
