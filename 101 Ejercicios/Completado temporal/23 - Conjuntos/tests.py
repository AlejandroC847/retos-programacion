"""Módulo para realizar las pruebas unitarias del módulo conjuntos.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
from conjuntos import sets

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_sets():
    """Verifica el funcionamiento de la lógica de conjuntos
    (intersección y diferencia simétrica).
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de lógica de conjuntos en 'sets()'...")

    set_a = [1, 2, 3, 4, 5]
    set_b = [3, 4, 5, 6, 7]

    # Caso por defecto
    assert sets(set_a, set_b) == [3, 4, 5]
    # Intersección (find_common=True)
    assert sets(set_a, set_b, True) == [3, 4, 5]
    # Diferencia simétrica (find_common=False)
    assert sets(set_a, set_b, False) == [1, 2, 6, 7]
    # Diferencia simétrica con una lista vacía
    assert sets(array_a=[1, 2, 3], find_common=False) == [1, 2, 3]

    # Listas vacías
    assert not sets() # Equivalente a == []
    # Diferencia simétrica con listas vacías
    assert not sets(find_common=False)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Válidaciones de expresiones esperadas.")

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    invalid_boolean_type_cases = (5, 9.81, [1, 2], {"tiempo": 2}, None, "Foo", (4, 5))
    invalid_non_list_inputs = (5, 9.81, "1 + 2", {"tiempo": 2}, True, (4, 5))

    for case in invalid_boolean_type_cases:
        with raises(TypeError):
            sets(find_common=case)

    for case in invalid_non_list_inputs:
        # Primer lista
        with raises(TypeError):
            sets(array_a=case)
        # Segunda lista
        with raises(TypeError):
            sets(array_b=case)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_sets()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
