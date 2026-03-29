"""
Moódulo para realizar las pruebas del módulo es_un_anagrama.py.
Se utiliza assert para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/03/29"

import es_un_anagrama as is_an
from colorama import Fore, Style

def test_is_anagram():
    """
    Ejecuta las pruebas esperadas para varios posibles casos dentro de la función is_anagram.
    """

    # Anagramas simples y con espacios
    res, status = is_an.is_anagram("hola", "Halo")
    assert res

    res, status = is_an.is_anagram("Roma!", "!amor")
    assert res

    res, status = is_an.is_anagram("Poderes","Es Pedro")
    assert res

    res, status = is_an.is_anagram("Tom Marvolo Riddle","I am Lord Voldemort")
    assert res

    res, status = is_an.is_anagram("     Montando","    montadon     ")
    assert res

    # No son anagramas
    res, status = is_an.is_anagram("Alberto","Velero")
    assert not res
    assert status == is_an.DIFF_LEN

    res, status = is_an.is_anagram("Carne","carNe")
    assert not res
    assert status == is_an.SAME_STR

    res, status = is_an.is_anagram("¿Halo?","Hola!")
    assert not res
    assert status == is_an.DIFF_LEN

    res, status = is_an.is_anagram("cima","maiz")
    assert not res
    assert status == is_an.STATUS_FAILED

    # Anagramas numericos
    res, status = is_an.is_anagram("171","117")
    assert res

    res, status = is_an.is_anagram("-251","15-2")
    assert res

    res, status = is_an.is_anagram("8.349 + 156 * (611 - 245)","3.141592654 * 8 + (-16)")
    assert res
def test_errores():
    """Realiza una prueba de errores posibles en la función is_anagram."""
    casos_a_fallar = [
        (("amor", "roma"),), # Tupla como un solo argumento
        (True, False),       # Booleanos
        ("texto", 2)         # String e Int
    ]

    for caso in casos_a_fallar:
        try:
            # Desempaquetamos los argumentos del caso
            is_an.is_anagram(*caso)
            assert False, f"Debería haber fallado con {caso}"
        except (TypeError, AttributeError):
            assert True

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    print("Ejecutando tests...")

    test_is_anagram()
    test_errores()

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
