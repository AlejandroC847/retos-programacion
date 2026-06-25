"""Módulo para realizar las pruebas unitarias del módulo clases.py.
Utiliza assert y pytest para verificar el correcto funcionamiento del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/24"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import clases as c

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_stack_class():
    """Verifica el comportamiento LIFO y los métodos de la clase Stack"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de  la clase Stack...")

    stack = c.Stack("A", "B", "C")
    assert stack.size == 3
    assert str(stack) == "Stack(['A', 'B', 'C'])"

    stack.add_element("D")
    assert stack.size == 4

    assert stack.pop_element() == "D"
    assert stack.size == 3

    assert stack.drain() == ["C", "B", "A"]
    assert stack.size == 0

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ La clase Stack funciona correctamente.")

def test_queue_class():
    """Verifica el comportamiento FIFO y los métodos de la clase Queue"""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de la clase Queue...")

    queue = c.Queue("1", "2", "3")
    assert queue.size == 3
    assert str(queue) == "Queue(['1', '2', '3'])"

    queue.add_element("4")
    assert queue.size == 4

    assert queue.pop_element() == "1"
    assert queue.size == 3

    assert queue.drain() == ["2", "3", "4"]
    assert queue.size == 0
    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Operaciones de cola (FIFO) correctas...")

def test_errores():
    """Verifica que el sistema lance una excepción ante valores inválidos (ValueError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    pila_vacia = c.Stack()
    with raises(ValueError):
        pila_vacia.pop_element()
    with raises(ValueError):
        pila_vacia.drain()

    cola_vacia = c.Queue()
    with raises(ValueError):
        cola_vacia.pop_element()
    with raises(ValueError):
        cola_vacia.drain()

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_stack_class()
        test_queue_class()

        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except (AssertionError, fail.Exception) as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
