"""Módulo que muestra el funcionamiento de la recursividad en python (llamado de una función a si
misma) imprimiendo los números de n a 0.
Tambien se integran con fines didacticos una función para obtener el resultado de _n!_ y
una función para obtener el elemento _n_ de la sucesión de Fibonacci
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/20"

import os
#import time
from functools import lru_cache


def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

def recursivity(n:int = 100):
    """Muestra una en pantalla la secuencia de números del 100 al 0.
    Utiliza la recursividad para disminuir el valor de n. Por defecto inicia en 100.

    Args:
        n (int, optional): Valor de n a imprimir y para que la función se llame recursivamente.
        Por defecto se establece n en 100.
    
    Raises:
        TypeError: Si el valor recibido no es un entero.
    """

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(
            "Se esperaba n como número entero."
            f"Se recibió {type(n).__name__}"
        )

    print(n, end="")

    if n == 0:
        print(".")
        return

    print(", ", end = "")
    if n > 0:
        recursivity(n - 1)
    else:
        recursivity(n + 1)

def factorial(n: int = 0) -> int:
    """Calcula el resultado de n!.

    Usa recursividad para obtener el factorial de n número llegando desde n hasta 0.
    Args:
        n (int, optional): Número a multiplicar por el resto de la sucesión.
        Por defecto es 0.

    Raises:
        TypeError: Si el valor recibido no es un entero.
        ValueError: Si el valor recibido es negativo.

    Returns:
        int: resultado de n!
    """

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(
            "Se requiere un número entero para n."
            f"Se recibió: {type(n).__name__}"
        )

    if n < 0:
        raise ValueError("El número debe ser positivo!")

    if n == 0:
        return 1
    return n * factorial(n - 1)

@lru_cache(maxsize=None) #Guarda el resultado de fibonacci(n) para ejecutarlo solo una vez
def fibonacci(n: int = 1):
    """Calcula el valor del elemento n en la sucesion de fibonacci

    La función se llama a si misma recursivamente con los valores n - 1 y n - 2 (los
    dos numeros anteriores en la sucesion) y retorna su suma.
    Args:
        n (int, optional): El valor a evaluar recursivamente. Por defecto es 0.

    Returns:
        int: El valor obtenido de la posición n en la sucesión fibonacci.
    """

    # La sucesion comienza con cero: 0, 1, 1, 2, 3, 5, 8...

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(
            "Se esperaba un número entero como argumento de posición."
            f"Se recibió: {type(n).__name__}"
        )

    if n <= 0:
        raise ValueError("El valor n debe ser mayor a 0!.")

    if n == 1:
        return 0

    if n == 2:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 07 - Recursividad")
    print("-" * 20)

    print("Sucesión de 100 a 0:")
    recursivity()


    print(f"\nResultado de 10!: {factorial(10)}")

    #inicio = time.time()
    print(f"\nEl elemento 500 de la serie Fibonacci es:\n{fibonacci(500)}")
    #fin = time.time()
    #print(f"La función tardó {fin-inicio:.6f} seg. en ejecutarse.")

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
