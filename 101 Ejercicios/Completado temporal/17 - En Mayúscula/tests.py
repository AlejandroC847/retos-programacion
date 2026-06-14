"""
Módulo para realizar las pruebas del módulo cuantos_dias.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/07"

import en_mayuscula as em
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_first_mayus():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función first_mayus()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'first_mayus()'...")

    # Una sola letra minúscula
    assert em.first_mayus("a") == "A"
    # Una sola palabra en minúsculas
    assert em.first_mayus("hola") == "Hola"
    # Frase estándar corta
    assert em.first_mayus("hola mundo") == "Hola Mundo"

    # Múltiples espacios seguidos entre palabras
    assert em.first_mayus("hola    mundo") == "Hola    Mundo"
    # Espacios al inicio y al final de la cadena
    assert em.first_mayus("   hola mundo   ") == "   Hola Mundo   "
    # Uso de tabulaciones (\t) y saltos de línea (\n)
    assert em.first_mayus("hola\tmundo\nnuevo") == "Hola\tMundo\nNuevo"

    # Palabra que inicia con un número
    assert em.first_mayus("16 dias") == "16 Dias"
    # Símbolos intermedios
    assert em.first_mayus("hola #mundo") == "Hola #mundo"
    # Correos electrónicos o rutas
    assert em.first_mayus("juan.perez@email.com") == "Juan.perez@email.com"
    assert em.first_mayus("C:/Users/usuario/Documents") == "C:/Users/usuario/Documents"

    # La cadena ya está correctamente capitalizada
    assert em.first_mayus("Hola Mundo") == "Hola Mundo"
    # Palabras que ya están COMPLETAMENTE en mayúsculas
    assert em.first_mayus("curso de PYTHON") == "Curso De PYTHON"
    # Cadena vacía
    assert em.first_mayus("") == ""
    # Cadena que consiste únicamente de espacios y tabulaciones
    assert em.first_mayus("  \t  \n ") == "  \t  \n "

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de modificacion de cadenas esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]

    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            em.first_mayus(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_first_mayus()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
