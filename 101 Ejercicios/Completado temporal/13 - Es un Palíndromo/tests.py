"""
Módulo para realizar las pruebas del módulo es_un_palindromo.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/07"

import es_un_palindromo as pal
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _limpiar_pantalla():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_palindrome():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función is_palindrome()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_palindrome()'...")

    assert pal.is_palindrome("oso")
    assert pal.is_palindrome("Radar")
    assert pal.is_palindrome("Anita lava la tina")
    assert pal.is_palindrome("¿Acaso hubo búhos acá?")
    assert pal.is_palindrome("12321")
    assert pal.is_palindrome("")
    # Casos Fallidos (False)
    assert not pal.is_palindrome("programacion")
    assert not pal.is_palindrome("hola")
    assert not pal.is_palindrome("123456")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de evaluación de palíndromos esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            pal.is_palindrome(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _limpiar_pantalla()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_palindrome()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
