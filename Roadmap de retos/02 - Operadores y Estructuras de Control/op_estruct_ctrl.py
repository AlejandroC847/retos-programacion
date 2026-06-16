"""Módulo para demostrar conceptos básicos de Python: operadores y estructuras de control.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/16"

import os

#pylint: disable=bad-chained-comparison

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def op_estruc():
    """Ejemplos de operadores y estructuras de control en Python"""

    print("Operadores: \n")

    print("\n\tOperadores Aritmeticos:")
    print(f"> Suma: 10 + 5 = {10 + 5}")
    print(f"> Resta: 6 - 2 = {6 - 2}")
    print(f"> Multiplicación: 3 * 4 = {3 * 4}")
    print(f"> División decimal: 10 / 3 = {10 / 3}")
    print(f"> División entera: 10 // 3 = {10 // 3}")
    print(f"> Módulo (Residuo): 24 % 5 = {24 % 5}")
    print(f"> Potecia: 2 ** 4 = {2 ** 4}")

    print("\n\tOperadores De Comparación:")
    print(f"El resultado : 10 > 5 es {10 > 5}")
    print(f"El resultado : 10 < 5 es {10 < 5}")
    print(f"El resultado : 21 <= 478519874269756194859781 es {21 <= 478519874269756194859781}")
    print(f"El resultado : 10 == 5 es {10 == 5}")
    print(f"El resultado : 10 != 5 es {10 != 5}")

    print("\n\tOperadores Lógicos:")
    print(f"El resultado de False and True: {False and True}")
    print(f"El resultado de False and False: {False and False}")
    print(f"El resultado de True and True: {True and True}")
    print(f"El resultado de True or False: {True or False}")
    print(f"El resultado de True or True: {True or True}")
    print(f"El resultado de not True: {not True}")
    print(f"El resultado de not False: {not False}")

    print("\n\tOperadores De Asignación:")
    print(f"El resultado de 6 += 3 es: {9}")
    print(f"El resultado de 12 -= 2 es: {10}")
    print(f"El resultado de 3 *= 5 es: {15}")
    print(f"El resultado de 25 /= 5 es: {5}")

    print("\n\tOperadores De Identidad:")
    print(f"El resultado de 1 == 1 is True: {(1 == 1) is True}") #noqa:F632
    print(f"El resultado de 3 is None: {3 is None}") #noqa:F632

    print("\n\tOperadores De Pertenencia:")
    print(f"El resultado de 3 in [1, 2, 3, 4, 5]: {3 in [1, 2, 3, 4, 5]}")
    print(f"El resultado de 8 in [10, 15, 20]: {8 in [10, 15, 20]}")

    print("\n\tOperadores De Bits (Bitwise):")
    print("a = 10  # 1010\nb = 6   # 0110\n")
    a = 10
    b = 6
        # AND
    resultado = a & b # El resultado es 2 (0010 en binario)
    print(f"AND (&) de {a} y {b} es: {resultado} ({bin(resultado)} en bin)")
        # OR
    resultado = a | b # El resultado es 14 (1110 en binario)
    print(f"OR (|) de {a} y {b} es: {resultado} ({bin(resultado)} en bin)")
        # XOR (OR Exclusivo, solo un bit es True)
    resultado = a ^ b # Resultado es 12 (1100 en binario)
    print(f"XOR (^) de {a} y {b} es: {resultado} ({bin(resultado)} en bin)")
        # NOT
    resultado = ~a # En binario, esto invierte la estructura completa.Resultado: -11
    print(f"NOT de {a} es: {resultado} ({bin(resultado)} en bin)")
        # DESPLAZAMIENTO
    print("\nDesplazamiento de n = 5 # Binario: 0101")
    n = 5
    print("Cada esplazamiento a la izquierda equivale a multiplicar por 2: 5 * 2 = 10")
    resultado = n << 1
    print(f"5 << 1 es: {resultado} ({bin(resultado)} en bin)") # Resultado: 10 (1010)
    resultado = n >> 1
    print("Cada esplazamiento a la derecha equivale a dividirsobre  2: 5 // 2 = 2")
    print(f"5 >> 1 es: {resultado} ({bin(resultado)} en bin)") # Resultado: 2 (0010)

    print("\n\nEstructuras de control:")

    print("\n\tCondicionales (if, elif, else):")
    print("> Mayor de edad: 18+")
    print("> Adolecenste: 13+")
    print("> Menor de edad: 12-")
    edad = 18
    print(f"La edad especificada es de {edad} años, por lo tanto...", end=" ")
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad > 13:
        print("Eres adolescente")
    else:
        print("Eres menor")

    print("\n\tEstructuras iterativas (Bucles):")
    print("\t\tFor:")
    # Bucle for
    for i in range(3):
        print(f"Repetición número {i}")
    print("\t\tWhile:")
    # Bucle while
    contador = 0
    while contador < 3:
        print(f"Contador: {contador}")
        contador += 1

    print("\n\tExcepciones:")
    try:
        resultado = 10 / 0
    except ZeroDivisionError as err:
        print(f"¡No puedes dividir entre cero!. {err}")
    finally:
        print("Esta parte se ejecuta siempre, haya error o no.")

    print("\nEjercicio adicional:\n")
    print("Crea un programa que imprima por consola todos los números comprendidos"
            "entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3")

    secuencia = ""
    for i in range(10, 56):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            secuencia += str(i) + ", "
    print(f"{secuencia[:-2:]}.")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 02 - Operadores y Estructuras de Control")
    print("-" * 20)

    op_estruc()

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
