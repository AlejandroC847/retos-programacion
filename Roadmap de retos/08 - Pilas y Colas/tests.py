"""Módulo para realizar las pruebas unitarias del módulo pilas_y_colas.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/23"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import pilas_y_colas as pc

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_stack_operations():
    """Verifica el funcionamiento adecuado de la Pila y el comportamiento LIFO"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para la Pila (Stack)...")

    stack = []
    pc.add_element_stack(stack, "A", "B", "C")
    assert stack == ["A", "B", "C"]
    assert pc.pop_element_stack(stack) == "C"
    assert pc.drain_stack(stack) == ["B", "A"]
    assert not stack

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Operaciones de pila (LIFO) correctas.")

def test_queue_operations():
    """Verifica el funcionamiento adecuado de la Cola y el comportamiento FIFO"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de cálculos para la Pila (Stack)...")

    queue = []
    pc.add_element_queue(queue, "1", "2", "3")
    assert queue == ["1", "2", "3"]
    assert pc.pop_element_queue(queue) == "1"
    assert pc.drain_queue(queue) == ["2", "3"]
    assert not queue

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Operaciones de cola (FIFO) correctas...")

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos (TypeError)
    o valores inválidos (ValueError).
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    invalid_list_type_cases = (True, 9.81, 1, {"tiempo": 2}, None, "8", (4, 5))

    for case in invalid_list_type_cases:
        with raises(TypeError):
            pc.add_element_stack(case)
            pc.pop_element_stack(case)
            pc.drain_stack(case)
            pc.add_element_queue(case)
            pc.pop_element_queue(case)
            pc.drain_queue(case)

    pila_vacia = []
    with raises(ValueError):
        pc.pop_element_stack(pila_vacia)
    with raises(ValueError):
        pc.drain_stack(pila_vacia)
    with raises(ValueError):
        pc.pop_element_queue(pila_vacia)
    with raises(ValueError):
        pc.drain_queue(pila_vacia)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_stack_operations()
        test_queue_operations()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
