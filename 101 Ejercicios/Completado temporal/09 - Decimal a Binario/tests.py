"""
Moódulo para realizar las pruebas del módulo decimal_a_binario.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/17"

import decimal_a_binario as dtob
from pytest import raises, fail
from colorama import Fore, Style, init

init(autoreset=True)

def tests_dec_a_bin():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función dec_a_bin()"""

    assert dtob.dec_a_bin(0) == [0]
    assert dtob.dec_a_bin(2) == [1, 0]
    assert dtob.dec_a_bin(255) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert dtob.dec_a_bin(170) == [1, 0, 1, 0, 1, 0, 1, 0]
    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Resultados de conteos esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    casos_invalidos_tipo = [3.14, True, "2", {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            dtob.dec_a_bin(caso)

    casos_invalidos_valor = [-1,-256,-84]
    for caso in casos_invalidos_valor:
        with raises(ValueError):
            dtob.dec_a_bin(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        tests_dec_a_bin()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
