"""Módulo para realizar las pruebas unitarias del módulo herencia_y_polimorfismo.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/25"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import herencia_y_polimorfismo as hp

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_errores():
    """Verifica que el sistema lance una excepción ante valores inválidos (ValueError) y 
    falta de permisos (PermissionError).
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    programador = hp.Programador("Luci", "666") #No puede emplear
    with raises(PermissionError):
        programador.emplear(hp.Empleado("", 0))

    gerente = hp.Gerente("Nina", "?")
    with raises(ValueError):
        gerente.emplear(5) #Intentar emplear algo que no sea Empleado

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
