"""Módulo para calcular el Máximo Común Divisor (MCD) y el Mínimo Común Múltiplo (mcm).
Proporciona funciones para realizar estos cálculos matemáticos utilizando el algoritmo
de Euclides y la relación entre el MCD y el mcm.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os
import sys

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def mcd(a: int, b: int) -> int:
    """Calcula el Máximo Común Divisor (MCD) de dos números enteros
    utilizando el algoritmo de Euclides.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: El Máximo Común Divisor de a y b.

    Raises:
        TypeError: Si alguno de los argumentos no es un entero.
        ValueError: Si ambos números son cero.
        """

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(
            f"El valor del número 'a' debe ser un número entero. Se recibió {type(a).__name__}"
        )
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(
            f"El valor del número 'b' debe ser un número entero. Se recibió {type(b).__name__}"
        )

    num_1, num_2 = abs(a), abs(b)

    if num_1 == 0 and num_2 == 0:
        raise ValueError(
            "El resultado de la operación está indefinido. Los dos números no pueden ser 0"
        )

    # Residuo anterior es 0
    if num_2 == 0:
        return num_1

    # Recursivamente calcula MCD
    # Eventualmente retornara el ultimo residuo diferente de 0
    return mcd(num_2, num_1 % num_2)

def mcm(a: int, b: int) -> int:
    """Calcula el Mínimo Común Múltiplo (mcm) de dos números enteros
    usando su propiedad fundamental en la teoría de números.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.

    Returns:
        int: El Mínimo Común Múltiplo de a y b.

    Raises:
        TypeError: Si alguno de los argumentos no es un entero.
        """

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError(
            f"El valor del número 'a' debe ser un número entero. Se recibió {type(a).__name__}"
        )
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError(
            f"El valor del número 'b' debe ser un número entero. Se recibió {type(b).__name__}"
        )

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // mcd(a, b)

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Máximo Común Divisor y Mínimo Común Múltiplo")
    print("-" * 20)

    a = b = None

    if len(sys.argv) == 3:
        try:
            a, b = map(int, sys.argv[1:])
            print(f"Usando argumentos de la línea de comandos: a = {a}, b = {b}.")
        except ValueError as err:
            print(f"Se introdujo un argumento inválido: {err}.")
            _enter_to_continue()
        except KeyboardInterrupt:
            print("Salida forzosa del programa. Interrupción del usuario.")
            return
    else:
        if len(sys.argv) > 3:
            print("Demasiados argumentos al ejecutar el programa.")
            _enter_to_continue()

        if len(sys.argv) == 2:
            print("Solo se paso un argumento al ejecutar el programa.")
            _enter_to_continue()

    if a is None or b is None:
        while True:
            _clear_console()
            print("-" * 20)
            print("Máximo Común Divisor y Mínimo Común Múltiplo")
            print("-" * 20)
            print("Recibiendo a la entrada del usuario...")

            try:
                a = int(input("Número entero 'a': "))
                b = int(input("Número entero 'b': "))
                break
            except ValueError as err:
                print(f"Se introdujo un argumento inválido: {err}.")
                _enter_to_continue()
            except KeyboardInterrupt:
                print("Salida forzosa del programa. Interrupción del usuario.")
                return

    try:
        res_mcd = mcd(a, b)
        res_mcm = mcm(a, b)

        print(f"\nEl mcm de {a} y {b} es: {res_mcm}.")
        print(f"El MCD de {a} y {b} es: {res_mcd}.\n")
    except ValueError as err:
        print(err)
    finally:
        _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
