"""
Moódulo para realizar las pruebas del módulo invirtiendo_cadenas.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/14"

import invirtiendo_cadenas as ic
from pytest import raises, fail
from colorama import Fore, Style, init

init(autoreset=True)

def test_invertir_cadena():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función invertir_cadena()"""

    assert ic.invertir_cadena("") == ""
    assert ic.invertir_cadena("Hola mundo") == "odnum aloH"
    assert ic.invertir_cadena("reconocer") == "reconocer"
    assert ic.invertir_cadena("4321") == "1234"

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Resultado de inversión esperado...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    casos_invalidos_bytes = [1.2, 987, True, None]

    for caso in casos_invalidos_bytes:
        with raises(TypeError):
            ic.invertir_cadena(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Pruebas de errores completadas con éxito.")

#=========================
#Ejecución Principal
#=========================
if __name__ == "__main__":
    try:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_invertir_cadena()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
