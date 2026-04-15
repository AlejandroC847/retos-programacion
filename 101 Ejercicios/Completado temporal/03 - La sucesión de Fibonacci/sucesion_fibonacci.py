"""
Muestra una lista de elementos de la serie Fibonacci.
La serie Fibonacci suma muestra en cada elemento la suma de sus dos elementos anteriores, siendo
sus únicas excepciones el 0 y el 1 iniciales. Un ejemplo de la serie es: 0, 1, 1, 2, 3, 5, 8, 13...
"""
__author__ = "Alejandro Cortés"
__date__ = "26/03/29"

from colorama import Fore, Style, init

init(autoreset=True)

# Formato de texto
CYAN = Fore.CYAN
GREEN = Fore.GREEN
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

def fibonacci_v1(n: int) -> int | None:
    """
    Calcula el n-ésimo número de la sucesión de Fibonacci de forma recursiva.

    La sucesión comienza con: 0, 1, 1, 2, 3, 5, 8, 13, 21...
    Donde:
    - F(1) = 0
    - F(2) = 1
    - F(n) = F(n-1) + F(n-2)
    
    Args:
        n (int): Posición del numero deseado dentro de la sucesión de Fibonacci (entero positivo).

    Returns:
        int | None: El valor entero del número Fibonacci en la posición n.
                    None si el parámetro no es un entero positivo.
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)

def fibonacci_v2(n: int) -> int | None:
    """
    Calcula el n-ésimo número de la sucesión de Fibonacci por medio del valor n y un bucle.

    F(1) = 0
    F(2) = 1
    F(n) = F(n-1) + F(n-2)

    Args:
        n (int): Posición del numero deseado dentro de la sucesión de Fibonacci (entero positivo).

    Returns:
        int | None: El valor entero del número Fibonacci en la posición n.
                    None si el parámetro no es un entero positivo.
    """

    if n <= 0 or isinstance(n, bool):
        return None

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

def print_fibonacci() -> None:
    """
    Muestra la lista de 50 elementos de la sucesión de fibonacci.
    """

    print(f"{CYAN}Ejercicio 03 - LA SUCESIÓN DE FIBONACCI{RESET}\n")
    print(f"{GREEN}Primeros 50 números:{RESET}")

    valores_a_mostrar = 50

    for i in range(1, valores_a_mostrar + 1):
        end_char = ", " if i < valores_a_mostrar else ".\n\n"
        print(f"{BRIGHT}{fibonacci_v2(i)}", end = end_char)

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    print_fibonacci()
