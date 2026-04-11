"""
Evalua si el número indicado es un número es o no primo.
Un número primo es un tipo de número natural (enteros positivos) que solo puede tener una división
entera sobre si mismo y sobre 1.
"""
__author__ = "Alejandro Cortés"
__date__ = "26/03/30"

from colorama import Fore, Style, init

init(autoreset=True)

# Formato de texto
CYAN = Fore.CYAN
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

def prime_number(num: int) -> bool | None:
    """

    Comprueba si un número en particular es un numero primo; es decir, un número natural que solo
    es divisible entre si mismo y entre 1.

    Args:
        num (int): Número entero positivo a evaluar.

    Returns:
        bool | None: Resultado de la evaluación de si es primo o no.
    """

    # Descarta valores no numericos
    if isinstance(num, bool):
        return None

    # Solo permite números enteros
    if not isinstance(num, int):
        return None

    # Solo positivos, de paso descarta 0 y 1
    if num < 2:
        return False

    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    return divisores == 2

def print_prime_numbers() -> None:
    """Solicita al usuario un número, llama a prime_number() para verificar si el número es
    primo o no y al final muestra el resultado."""

    print(f"{CYAN}Ejercicio 03 - LA SUCESIÓN DE FIBONACCI{RESET}\n")

    num = int(input("Ingrese número: "))

    res = prime_number(num)
    msg = {"Es primo" if res else ("NO es primo" if res is False else "Dato inválido")}

    print(f"#{num}: {msg}")

def print_from_1_to_100():
    """Imprime en pantalla todos los números primos entrte 1 y 100"""
    primos = []
    for i in range(1,100):
        if prime_number(i):
            primos.append(str(i))

    print(", ".join(primos) + ".")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    print_from_1_to_100()
