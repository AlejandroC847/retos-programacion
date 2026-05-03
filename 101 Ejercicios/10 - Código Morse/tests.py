"""
Moódulo para realizar las pruebas del módulo codigo_morse.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/28"

import codigo_morse as cm
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)
def limpiar_pantalla():
    """Limpia la consola de comandos dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_morse():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función is_morse()"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_morse()'...")

    # True
    assert cm.is_morse("..---..")
    assert cm.is_morse("////////")
    assert cm.is_morse("        ")
    assert cm.is_morse("")

    # False
    assert not cm.is_morse("abc")
    assert not cm.is_morse("123")
    assert not cm.is_morse(".-/ a")
    assert not cm.is_morse("/.??")
    assert not cm.is_morse("\n")
    assert not cm.is_morse("\t")
    assert not cm.is_morse("...___...")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de comprobación de morse esperados...")

def test_nat_to_morse():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función nat_to_morse()"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'nat_to_morse()'...")

    assert  cm.nat_to_morse("sos") == "... --- ..."
    assert  cm.nat_to_morse("sos sos") == "... --- ...   ... --- ..."
    assert  cm.nat_to_morse("Hola mundo") == ".... --- .-.. .-   -- ..- -. -.. ---"
    assert  cm.nat_to_morse("?") == "..--.."
    assert  cm.nat_to_morse("847") == "---.. ....- --..."
    assert  cm.nat_to_morse("  ") == "   "
    assert  cm.nat_to_morse("") == ""

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de traducción a morse esperados...")

def test_morse_to_nat():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función morse_to_nat()"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'morse_to_nat()'...")

    assert  cm.morse_to_nat("... --- ...") == "SOS"
    assert  cm.morse_to_nat(".... --- .-.. .-   -- ..- -. -.. ---") == "HOLA MUNDO"
    assert  cm.morse_to_nat("- ..-/-.--/-.-- ---") == "TU Y YO"
    assert  cm.morse_to_nat(".-///-...") == "A B"
    assert  cm.morse_to_nat("//////") == ""
    assert  cm.morse_to_nat("  ") == ""
    assert  cm.morse_to_nat("") == ""

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de traducción a LN esperados...")

def test_errores():
    """
        Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            # Las funciones esperan cadenas de texto, no otros tipos de datos
            cm.morse_to_nat(caso)
        with raises(TypeError):
            cm.nat_to_morse(caso)
        with raises(TypeError):
            cm.is_morse(caso)

    # Pruebas para nat_to_morse con caracteres no soportados
    casos_invalidos_nat = ["Hola!", "áéíóú", "Python @"]
    for caso in casos_invalidos_nat:
        with raises(ValueError):
            cm.nat_to_morse(caso)

    # Pruebas para morse_to_nat con secuencias morse no válidas
    casos_invalidos_morse = ["...---...", ".-.-.---", "--. .--.-", "ABC", ".-.-.-.-.-.-."]
    for caso in casos_invalidos_morse:
        with raises(ValueError):
            cm.morse_to_nat(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")


# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        limpiar_pantalla()
        print(f"{Fore.CYAN}{'='*40}")

        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_morse()
        test_nat_to_morse()
        test_morse_to_nat()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
