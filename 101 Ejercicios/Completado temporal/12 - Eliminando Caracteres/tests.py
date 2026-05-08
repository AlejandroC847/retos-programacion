"""
Módulo para realizar las pruebas del módulo eliminando_caracteres.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/05"

import eliminando_caracteres as ec
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _limpiar_pantalla():
    """Limpia la consola de comandos dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_eliminar_caracteres():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función eliminar_caracteres()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'eliminar_caracteres()'...")

    # Caso 1: Cadenas idénticas (debe retornar cadenas vacías)
    assert ec.eliminar_caracteres("python", "python") == ("", "")

    # Caso 2: Ambas cadenas vacías
    assert ec.eliminar_caracteres("", "") == ("", "")

    # Caso 3: Una cadena vacía (retorna caracteres únicos de la otra, ordenados)
    assert ec.eliminar_caracteres("banana", "") == ("abn", "")
    assert ec.eliminar_caracteres("", "hola") == ("", "ahlo")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de eliminar caracteres esperados...")

def test_filtrar_caracteres():
    """
        Ejecuta las pruebas esperadas por posibles casos aplicados a
        la función filtrar_caracteres()
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'filtrar_caracteres()'...")

    # Caso 1: Cadenas idénticas (debe retornar cadenas vacías)
    assert ec.filtrar_caracteres("python", "python") == ("", "")

    # Caso 2: Ambas cadenas vacías
    assert ec.filtrar_caracteres("", "") == ("", "")

    # Caso 3: Una cadena vacía (retorna caracteres únicos de la otra, ordenados)
    assert ec.filtrar_caracteres("banana", "") == ("banana", "")
    assert ec.filtrar_caracteres("", "hola") == ("", "hola")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de eliminar caracteres esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ec.eliminar_caracteres(caso, "cadena_valida")
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ec.eliminar_caracteres("cadena_valida", caso)

    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ec.filtrar_caracteres(caso, "cadena_valida")
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ec.filtrar_caracteres("cadena_valida", caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _limpiar_pantalla()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_eliminar_caracteres()
        test_filtrar_caracteres()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
