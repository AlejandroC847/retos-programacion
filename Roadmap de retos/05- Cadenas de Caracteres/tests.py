"""Módulo para realizar las pruebas unitarias del módulo cadenas_de_caracteres.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/19"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import cadenas_de_caracteres as cc

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_anagram():
    """Verifica el funcionamiento de la evaluación de anagrama"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para 'is_anagram()'...")

    # Anagramas simples y con espacios
    res, status = cc.is_anagram("hola", "Halo")
    assert res

    res, status = cc.is_anagram("Roma!", "!amor")
    assert res

    res, status = cc.is_anagram("Poderes","Es Pedro")
    assert res

    res, status = cc.is_anagram("Tom Marvolo Riddle","I am Lord Voldemort")
    assert res

    res, status = cc.is_anagram("     Montando","    montadon     ")
    assert res
    assert status == "SON un anagrama"

    # No son anagramas
    res, status = cc.is_anagram("Alberto","Velero")
    assert not res
    assert status == "Diferente longitud! Cadenas inválidas!"

    res, status = cc.is_anagram("Carne","carNe")
    assert not res
    assert status == "Es la misma cadena, NO son un anagrama."

    res, status = cc.is_anagram("¿Halo?","Hola!")
    assert not res
    assert status == "Diferente longitud! Cadenas inválidas!"

    res, status = cc.is_anagram("cima","maiz")
    assert not res
    assert status == "NO son un anagrama"

    # Anagramas numericos
    res, status = cc.is_anagram("171","117")
    assert res

    res, status = cc.is_anagram("-251","15-2")
    assert res

    res, status = cc.is_anagram("8.349 + 156 * (611 - 245)","3.141592654 * 8 + (-16)")
    assert res

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Evaluaciones de anagramas esperadas.")

def test_is_palindrome():
    """Verifica el funcionamiento de la evaluación de palíndromos"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_palindrome()'...")

    assert cc.is_palindrome("oso")
    assert cc.is_palindrome("Radar")
    assert cc.is_palindrome("Anita lava la tina")
    assert cc.is_palindrome("¿Acaso hubo búhos acá?")
    assert cc.is_palindrome("12321")
    assert cc.is_palindrome("")
    # Casosccllidos (False)
    assert not cc.is_palindrome("programacion")
    assert not cc.is_palindrome("hola")
    assert not cc.is_palindrome("123456")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de evaluación de palíndromos esperados...")

def test_is_isogram():
    """Verifica el funcionamiento de la evaluación de isogramas"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_isogram()'...")

    assert cc.is_isogram("cielo")
    assert cc.is_isogram("cénit")
    assert cc.is_isogram("Humano")
    assert cc.is_isogram("Muy Fan")
    assert cc.is_isogram("Humo-Pez")
    assert cc.is_isogram("")
    # Casosccllidos (False)
    assert not cc.is_isogram("Carta")
    assert not cc.is_isogram("hola-mundo")
    assert not cc.is_isogram("Área")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de evaluación de isogramas esperados...")

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    invalid_str_type_cases = (True, 9.81, [1, 2], {"tiempo": 2}, None, 8, (4, 5))

    for case in invalid_str_type_cases:
        with raises(TypeError):
            cc.is_anagram(case, "")
            cc.is_anagram("", case)
            cc.is_palindrome(case)
            cc.is_isogram(case)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_anagram()
        test_is_palindrome()
        test_is_isogram()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
