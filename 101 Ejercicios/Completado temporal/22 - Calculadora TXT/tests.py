"""Módulo para realizar las pruebas unitarias del módulo calculadora_txt.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del validador,
el motor de cálculo lineal y el manejo de archivos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/13"

import os
from pathlib import Path
from pytest import raises, fail
from colorama import Fore, Style, init
import calculadora_txt as calc

TEST_FILE = "test.txt"

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_validate_expression():
    """Verifica que las validaciones de las expresiones tengan el resultado esperado."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de flujo en 'validate_expression()'...")

    assert calc.validate_expression("1 + 2 + 3 + 4 + 5")
    assert calc.validate_expression("2 + 4 - 6 * 8 / 10")
    assert calc.validate_expression("1")

    # Las expresiones invalidas lanzan directamente una excepcion

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Válidaciones de expresiones esperadas.")

def test_calc_txt():
    """Verifica que la función calc_txt realice los cálculos correctamente."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de motor de cálculo en 'calc_txt()'...")

    # Suma convencional
    calc.write_file(TEST_FILE, "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10".split())
    assert calc.calc_txt(TEST_FILE) == ("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10", 55.0)

    # Todas las operaciones
    calc.write_file(TEST_FILE, "2 + 4 - 6 * 8 / 10".split())
    assert calc.calc_txt(TEST_FILE) == ("2 + 4 - 6 * 8 / 10", 0.0)

    #Numero individual
    calc.write_file(TEST_FILE, "847".split())
    assert calc.calc_txt(TEST_FILE) == ("847", 847.0)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Cálculos de operaciones esperados.")

def test_read_file():
    """Verifica que la lectura de archivos funcione correctamente y maneje errores de tipo."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}"
        "Ejecutando pruebas de lectura de archivos en 'read_file()'..."
    )

    # Prueba de lectura exitosa
    content = ["10", "+", "20"]
    calc.write_file(TEST_FILE, content)
    assert calc.read_file(TEST_FILE) == content

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Lectura de archivos realizada correctamente.")


def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError),
    ante caracteres no permitidos u operaciones prohibidas(ValueError) o
    errores en la lectura del archivo (FileNotFoundError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    casos_invalidos_not_str = (5, 9.81, [1, 2], {"tiempo": 2}, None, True, (4, 5))
    casos_invalidos_not_list = (5, 9.81, "1 + 2", {"tiempo": 2}, None, True, (4, 5))

    # TypeError
    for caso in casos_invalidos_not_str:
        with raises(TypeError):
            calc.validate_expression(caso)
        with raises(TypeError):
            calc.read_file(caso)
        with raises(TypeError):
            calc.write_file(caso, ["1"])
        with raises(TypeError):
            calc.write_file("archivo", [caso])

    for caso in casos_invalidos_not_list:
        with raises(TypeError):
            calc.write_file("archivo", caso)

    with raises(ValueError):
        calc.write_file(TEST_FILE, ["5", "/", "0"])
        calc.calc_txt(TEST_FILE)
    with raises(ValueError):
        calc.validate_expression("")
    with raises(ValueError):
        calc.validate_expression("a + b")
    with raises(ValueError):
        calc.validate_expression("1 % 2")
    with raises(ValueError):
        calc.validate_expression("1 + 2 + ")

    # Eliminar archivo de pruebas
    test_file_root = Path(__file__).resolve().parent / TEST_FILE
    if test_file_root.exists():
        test_file_root.unlink()

    with raises(FileNotFoundError):
        calc.read_file(TEST_FILE)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_validate_expression()
        test_calc_txt()
        test_read_file()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
