"""
Moódulo para realizar las pruebas del módulo fizzbuz.py.
Se utiliza assert para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/03/23"

import fizzbuzz as fb

def test_fizzbuzz():
    """
    Ejecuta las pruebas esperadas para varios posibles casos dentro de la función fizzbuzz.
    """

    # Casos normales
    assert fb.fizzbuzz(1) == "1"
    assert fb.fizzbuzz(2) == "2"

    # Múltiplos de 3
    assert fb.fizzbuzz(3) == "fizz"
    assert fb.fizzbuzz(6) == "fizz"

    # Múltiplos de 5
    assert fb.fizzbuzz(5) == "buzz"
    assert fb.fizzbuzz(10) == "buzz"

    # Múltiplos de ambos
    assert fb.fizzbuzz(15) == "fizzbuzz"
    assert fb.fizzbuzz(30) == "fizzbuzz"

    # Números negativos
    assert fb.fizzbuzz(-2) == "-2"
    assert fb.fizzbuzz(-3) == "fizz"
    assert fb.fizzbuzz(-5) == "buzz"
    assert fb.fizzbuzz(-15) == "fizzbuzz"

def test_errores():
    """Realiza una prueba de errores posibles en la función fizzbuzz."""
    try:
        fb.fizzbuzz("hola")
    except TypeError:
        assert True
    else:
        assert False, "Se esperaba TypeError"

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    print("Ejecutando tests...")

    test_fizzbuzz()
    test_errores()

    print("✅ Todos los tests pasaron correctamente")
