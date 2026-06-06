"""Módulo que calcula el factorial de un número de forma recursiva.
El factorial de un entero positivo n, se define como el producto de todos 
los números enteros positivos desde 1 hasta n.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/08"

import os
import sys
from inspect import stack

def _clear_console():
    # Limpia la pantalla
    os.system("cls" if os.name == "nt" else "clear")

def factorial_recursivo(n: int)-> int:
    """Calcula el factorial de un número entero positivo de forma recursiva.

    Args:
        n (int): El número entero del cual se desea calcular el factorial.

    Returns:
        int: El resultado del factorial de n.
    Raises:
        TypeError: Si la entrada no es un número entero.
        ValueError: Si el número es negativo.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Se requiere de un número entero positivo.")

    if n < 0:
        raise ValueError("El número debe ser un entero positivo!.")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def _main():
    # Demo del programa.

    _clear_console()

    if len(sys.argv) > 2:
        print("Se esperaba solo un número entero positivo")
        return
    if len(sys.argv) == 2:
        print("-" * 20)
        print("Factorial recursivo")
        print("-" * 20)

        res  = factorial_recursivo(int(sys.argv[1]))
        print(res)
    else:
        while True:
            _clear_console()
            print("-" * 20)
            print("Factorial recursivo")
            print("-" * 20)
            try:
                print(f"Límite de Recursiones: {sys.getrecursionlimit() - len(stack())}")

                num = int(input("Escribe un número: "))
                res = factorial_recursivo(num)
                print(f"{num}! = {res}.\n")
                break
            except ValueError:
                print("¡Error! Debes ingresar un número entero (sin letras ni decimales).")
                input("Enter para Continuar...")
            except RecursionError:
                print("¡Error! Excediste la cantidad de recursiones. Verifica el límite.")
                input("Enter para Continuar...")
            except KeyboardInterrupt:
                print("\nPrograma cancelado por el usuario.")
                break

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
