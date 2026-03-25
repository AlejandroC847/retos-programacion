def fizzbuzz(n: int) -> str:
    """
    Devuelve la representación de un número según las reglas de FizzBuzz.

    - Múltiplos de 3 → "fizz"
    - Múltiplos de 5 → "buzz"
    - Múltiplos de ambos → "fizzbuzz"
    - En otro caso → el número como string

    Args:
        n (int): Número a evaluar

    Returns:
        str: Resultado según reglas FizzBuzz

    Raises:
        TypeError: Si n no es un entero
    """
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un entero")

    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"

    return str(n)

def ejecutar_fizzbuzz(inicio: int = 1, fin: int = 100) -> None:
    """
    Imprime la secuencia FizzBuzz en consola.

    Args:
        inicio (int): Inicio del rango
        fin (int): Fin del rango
    """
    for i in range(inicio, fin + 1):
        print(fizzbuzz(i))

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    ejecutar_fizzbuzz()