"""Módulo que determina si un número es un número de Armstrong.
Un número de Armstrong (o narcisista) es aquel que es igual a la suma de sus 
propios dígitos elevados a la potencia del número de dígitos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/09"

import sys
import os

def _clear_console():
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

def is_armstrong(num: int) -> bool:
    """Determina si un número entero es un número de Armstrong.
    Un número de Armstrong es aquel que es igual a la suma de sus propios dígitos 
    elevados a la potencia del número de dígitos.

    Args:
        num (int): Número natural a evaluar.

    Raises:
        TypeError: Si el argumento no es un número entero.
        ValueError: Si el argumento no es un número no negativo.

    Returns:
        bool: True si 'num' es narcisista (Armstrong), False en caso contrario.
    """

    if isinstance(num, bool) or not isinstance(num, int):
        raise TypeError("Se requiere de un número entero no negativo.")

    if num < 0:
        raise ValueError("El número debe ser un entero no negativo!.")

    num_str = str(num)
    digitos = len(num_str)
    suma = sum(int(digito) ** digitos for digito in num_str)

    return suma == num

def _main():
    # Demo del programa.

    _clear_console()

    if len(sys.argv) > 2:
        print("Se esperaba solo un número entero no negativo")
        return
    if len(sys.argv) == 2:
        print("-" * 20)
        print("Número de Armstrong")
        print("-" * 20)

        print(f"El Número {sys.argv[1]} "
            f"{"SI" if is_armstrong(int(sys.argv[1])) else "NO"} "
            "es un número narcisista (de Armstrong).\n"
            )
    else:
        while True:
            _clear_console()
            print("-" * 20)
            print("Número de Armstrong")
            print("-" * 20)
            try:
                num = int(input("Escribe un número: "))
                print(f"El Número {num} "
                    f"{"SI" if is_armstrong(num) else "NO"} "
                    "es un número narcisista (de Armstrong).\n")
                break
            except ValueError:
                print("¡Error! Debes ingresar un número entero (sin letras ni decimales).")
                input("Enter para Continuar...")
            except KeyboardInterrupt:
                print("\nPrograma cancelado por el usuario.")
                break

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
