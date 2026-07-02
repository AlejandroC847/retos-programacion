"""Módulo para realizar las pruebas unitarias del módulo manejo_de_ficheros.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/07/01"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import manejo_de_ficheros as mf

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_errores():
    """Verifica que el sistema lance una excepción ante valores inválidos (ValueError) y 
    falta de permisos (PermissionError).
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    admin = mf.SalesManager()

    with raises(TypeError):
        admin._product_exist(5)

    with raises(TypeError):
        admin.add_products(casa=9)
    with raises(TypeError):
        admin.add_products(casa={"error":6.4})
    with raises(TypeError):
        admin.add_products(casa={"precio": 1500, "units_sold":-5})
    with raises(TypeError):
        admin.add_products(casa={"precio":-5, "units_sold": 10})

    admin.products = {"tv": {"price": 1, "units_sold": 1}}
    with raises(TypeError):
        admin.update_product(8, 15.5, 10)
    with raises(ValueError):
        admin.update_product("tv", "s", 10)
    with raises(ValueError):
        admin.update_product("tv", 15.5, -8)

    with raises(TypeError):
        admin.delete_product(-8)

    admin.clean_inventory()

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
