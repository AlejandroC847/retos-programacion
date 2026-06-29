"""Módulo para realizar las pruebas unitarias del módulo excepciones.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/28"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import excepciones as ex

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_funcion_prueba_type_error():
    """Verifica que lance TypeError si el primer argumento no es string."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores (TypeError)...")
    with raises(TypeError):
        # Pasamos un entero donde se esperaba un string
        ex.funcion_prueba(123, 10)
    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de (TypeError) completadas con éxito.")

def test_funcion_prueba_value_error():
    """Verifica que lance ValueError si el segundo argumento es negativo."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores (ValueError)...")
    with raises(ValueError, match="El primer argumento debe ser un número positivo."):
        ex.funcion_prueba("Contraseña", -5)
    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de (ValueError) completadas con éxito.")

def test_funcion_prueba_mi_error_personalizado():
    """Verifica que lance nuestra excepción personalizada correctamente."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}"
        "Ejecutando pruebas de manejo de errores (MiErrorPersonalizado)..."
    )
    with raises(ex.MiErrorPersonalizado) as excinfo:
        ex.funcion_prueba("PalabraIncorrecta", 10)
    # Verificamos que el código de error sea el esperado
    assert excinfo.value.error_code == 1
    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de (MiErrorPersonalizado) completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_funcion_prueba_type_error()
        test_funcion_prueba_value_error()
        test_funcion_prueba_mi_error_personalizado()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
