"""
Moódulo para realizar las pruebas del módulo contando_palabras.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/17"

import contando_palabras as copa
from pytest import raises, fail
from colorama import Fore, Style, init

init(autoreset=True)

def tests_contar_palabras():
    """Ejecuta las pruebas esperadas por posibles casos aplicados a la función contar_palabras()"""

    assert copa.contar_palabras(
        "Don Juan don't have a T-shirt"
        ) == {
                "don": 2,
                "juan": 1,
                "t": 2,
                "have": 1,
                "a": 1,
                "shirt": 1
            }
    assert copa.contar_palabras(
        "En 2026, México ganará... ¡o eso espero! 100% real."
        ) == {
                "en": 1,
                "2026": 1,
                "méxico": 1,
                "ganará": 1,
                "o": 1,
                "eso": 1,
                "espero": 1,
                "100": 1,
                "real": 1
            }
    assert copa.contar_palabras(
        "El Papa come papa, pero mi papá no come papa."
        ) == {
                "el": 1,
                "papa": 3,
                "come": 2,
                "pero": 1,
                "mi": 1,
                "papá": 1,
                "no": 1
            }
    assert copa.contar_palabras(
        "¿Hola???... ¡¡¡Hola!!!     (¿hay alguien ahí?)"
        ) == {
                "hola": 2,
                "hay": 1,
                "alguien": 1,
                "ahí": 1
            }
    assert copa.contar_palabras(
        "Usuario_C847 dice: 'x = 10 / 2 + (5*5)'"
        ) == {
                "usuario": 1,
                "c847": 1,
                "dice": 1,
                "x": 1,
                "10": 1,
                "2": 1,
                "5": 2
            }

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Resultados de conteos esperados...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    casos_invalidos_tipo = [1, 3.14, True, {"uno": 1}, [3, 4, 5], None]
    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            copa.contar_palabras(caso)

    casos_invalidos_valor = ["", "  ?  ", "...."]
    for caso in casos_invalidos_valor:
        with raises(ValueError):
            copa.contar_palabras(caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Pruebas de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        tests_contar_palabras()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
