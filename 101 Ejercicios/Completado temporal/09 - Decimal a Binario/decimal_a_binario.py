"""Convierte un número decimal a un número binario usando el método de divisiones sucesivas."""
__author__ = "Alejandro Cortés"
__date__ = "2026/4/20"

def dec_a_bin(num: int) -> list:
    """Convierte un número de decimal a una lista de bits.

    Args:
        num (int): Número entero positivo.

    Raises:
        TypeError: Se lanza un error de tipo si no se recibe un número entero.
        ValueError: Se lanza un error de valor si es un número negativo.

    Returns:
        list: Lista de bits equivalente al decimal en binario.
    """

    if isinstance(num, bool) or not isinstance(num, int):
        raise TypeError("Solo se aceptan números enteros")

    if num < 0:
        raise ValueError("Solo se aceptan números enteros")
    elif num == 0:
        return [0]

    binario = []

    while num > 0:
        binario.append(num % 2)
        num = num // 2

    binario.reverse()

    return binario

def lista_bin_a_str(lista_bin: list) -> str:
    """Convierte una lista de bits en una cadena de texto.

    Args:
        lista_bin (list): Cadena de bits inicial.

    Returns:
        str: Cadena de texto que representa el número binario.
    """

    if not isinstance(lista_bin, list):
        raise TypeError("Se esperaba una lista de enteros")

    bin_str = ""

    while len(lista_bin) > 0:
        bin_str += str(lista_bin.pop(0))

    return bin_str

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    NUM_BIN = lista_bin_a_str(dec_a_bin(83)) #1100101
    print(f"Binario: {NUM_BIN}")
