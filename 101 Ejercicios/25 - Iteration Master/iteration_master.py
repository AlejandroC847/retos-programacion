"""Módulo para demostrar diferentes formas de iterar en Python.
Muestra métodos como for, while, recursividad, listas, itertools, clases, exec y eval.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os
from functools import partial
import itertools as it

MIN = 1
MAX = 100

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def _get_sep(num: int) -> str:
    """Obtiene el tipo de separador requerido para la posicion del número.

    Args:
        num (int): Número a evaluar.

    Returns:
        str: Separador ", " si es un número inicial o intermedio.
            Separador ".\\n" si es el ultimo número. 
    """
    return ', ' if num < MAX else '.\n'

def iteration_for():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando un bucle for."""

    print("Método For:", end=" ")

    for i in range(MIN, MAX + 1):
        print(i, end=_get_sep(i))

def iteration_while():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando un bucle while."""

    print("Método While:", end=" ")
    num = MIN

    while num <= MAX:
        print(num, end=_get_sep(num))
        num += 1

def iteration_recursive(num: int = MAX):
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando una función recursiva."""

    if num < MIN:
        print("Método Recursivo:", end=" ")
    else:
        iteration_recursive(num - 1)
        print(num, end=_get_sep(num))

def iteration_list():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando una lista."""

    print("Método de Lista:", end=" ")

    lista = [str(i) + _get_sep(i) for i in range(MIN, MAX + 1)]

    print_empty = partial(print, end="")

    # list(map(lambda x: print(x, end=""), lista))  # Función Lambda
    list(map(print_empty, lista))                   # Función partial del módulo functools

def iteration_stdlib():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando
    la biblioteca estándar itertools.
    """

    print("Método de Biblioteca estándar (itertools):", end=" ")

    flujo_infinito = it.count(MIN, 1)
    flujo_cortado = it.islice(flujo_infinito, MAX - MIN + 1)

    print(*[str(i) + _get_sep(i) for i in flujo_cortado], sep="", end= "")

def iteration_class():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando una clase personalizada."""

    class IteratorClass():
        """Iterador personalizado que recorre los números del MIN al MAX."""
        def __init__(self):
            self.max = MAX
            self.num = MIN - 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.num >= self.max:
                raise StopIteration
            self.num += 1
            return self.num

    print("Método de Clase Personalizada:", end=" ")

    iterador = IteratorClass()

    for x in iterador:
        print(f"{x}{_get_sep(x)}", end = "")

def iteration_exec():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando la funcion exec()."""

    print("Método de exec():", end=" ")

    lista_comandos = [
        f"print({i}, end='{_get_sep(i).replace('\n', '\\n')}')"
        for i in range(MIN, MAX + 1)
    ]
    comando_final = "\n".join(lista_comandos)

    #pylint: disable=exec-used
    exec(comando_final)

def iteration_eval():
    """Itera desde MIN hasta MAX imprimiendo cada número utilizando la funcion eval()."""

    print("Método de eval():", end=" ")

    expresion = "[print(i, end=_get_sep(i)) for i in range(MIN, MAX + 1)]"

    #pylint: disable= eval-used
    eval(expresion, globals())

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Iteration Master")
    print("-" * 20)

    iteration_for()
    iteration_while()
    iteration_recursive()
    iteration_list()
    iteration_stdlib()
    iteration_class()
    iteration_exec()
    iteration_eval()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
