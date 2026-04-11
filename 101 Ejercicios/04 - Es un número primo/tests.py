"""
Moódulo para realizar las pruebas del módulo numero_primo.py.
Se utiliza assert para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/10"

import numero_primo as prime
from colorama import Fore, Style, init

init(autoreset=True)

def test_primos():
    """    Ejecuta las pruebas esperadas por posibles casos dentro de la funcion prime_number()"""

    # Números Primos
    assert prime.prime_number(2)
    assert prime.prime_number(3)
    assert prime.prime_number(5)
    assert prime.prime_number(7)
    assert prime.prime_number(101)

    # Números no primos y casos especiales
    assert not prime.prime_number(0)
    assert not prime.prime_number(-0)
    assert not prime.prime_number(1)
    assert not prime.prime_number(28)
    assert not prime.prime_number(-22)
    assert not prime.prime_number(-5)

def test_errores():
    """Verifica que la función maneje correctamente entradas de tipos inválidos."""
    casos_invalidos = [
        "Once",         # String
        "13",           # String numérico
        5.6,            # Float
        True,           # Booleano
        False,          # Booleano
        [7],            # Lista
        None            # NoneType
    ]

    for caso in casos_invalidos:
        resultado = prime.prime_number(caso)
        # Verificamos que nuestro "filtro" interno devolvió None
        assert resultado is None, f"Debería haber retornado None para {type(caso).__name__}: {caso}"

#=========================
#Ejecución Principal
#=========================
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}Ejecutando tests...")

    test_primos()
    test_errores()

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
