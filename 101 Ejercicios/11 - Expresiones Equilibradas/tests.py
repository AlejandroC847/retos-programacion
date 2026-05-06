"""
Módulo para realizar las pruebas del módulo expresiones_equilibradas.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/05"

import expresiones_equilibradas as ee
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def limpiar_pantalla():
    """Limpia la consola de comandos dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_balanced():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función is_balanced()"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_balanced()'...")

    assert ee.is_balanced("{a + [(b - 3) * c] / (d + e)}")
    assert ee.is_balanced("a + c")
    assert ee.is_balanced("")
    assert ee.is_balanced("((((()))))")
    assert ee.is_balanced("{{[[(())]]}}")
    assert ee.is_balanced("()[]{}")

    assert not ee.is_balanced(")a + b(")
    assert not ee.is_balanced("(()")
    assert not ee.is_balanced("(()")
    assert not ee.is_balanced("{[(])}")
    assert not ee.is_balanced("([)]")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de comprobación de balanceo de ecuaciones esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ee.is_balanced(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        limpiar_pantalla()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_balanced()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
