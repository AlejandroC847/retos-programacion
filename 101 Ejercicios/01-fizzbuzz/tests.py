from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    # Casos normales
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

    # Múltiplos de 3
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"

    # Múltiplos de 5
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"

    # Múltiplos de ambos
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(30) == "fizzbuzz"
    
    # Números negativos
    assert fizzbuzz(-2) == "-2"
    assert fizzbuzz(-3) == "fizz"
    assert fizzbuzz(-5) == "buzz"
    assert fizzbuzz(-15) == "fizzbuzz"

def test_errores():
    try:
        fizzbuzz("hola")
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