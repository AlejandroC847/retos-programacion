"""
Moódulo para realizar las pruebas del módulo sucesion_fibonacci.py.
Se utiliza assert para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/03/29"


import sucesion_fibonacci as fib
from colorama import Fore, Style

def test_fibonacci():
    """
    Ejecuta las pruebas esperadas para varios posibles casos dentro de la función fibonacci.
    """

    # Anagramas simples y con espacios
    assert fib.fibonacci_v2(50) == 7778742049
    assert fib.fibonacci_v2(10) == 34
    assert fib.fibonacci_v2(3) == 1
    assert fib.fibonacci_v2(2) == 1
    assert fib.fibonacci_v2(1) == 0
    assert fib.fibonacci_v2(0) is None
    assert fib.fibonacci_v2(-5) is None
    assert fib.fibonacci_v2(False) is None
    assert fib.fibonacci_v2(True) is None

def test_errores():
    """Realiza una prueba de errores posibles en la función fibonacci."""
    casos_a_fallar = [
        "cincuenta",    # String simple
        "50",           # String que aparenta un número
        10.3            # Float
    ]

    for caso in casos_a_fallar:
        try:
            # Desempaquetamos los argumentos del caso
            fib.fibonacci_v2(caso)
            assert False, f"Debería haber fallado con {caso}"
        except TypeError:
            assert True

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}Ejecutando tests...")

    test_fibonacci()
    test_errores()

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
