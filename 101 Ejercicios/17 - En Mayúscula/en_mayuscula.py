""" Módulo encargado de cambiar las inciales de cada palabra de una cadena de texto.

A partir de una cadena de texto cambia la primer letra de cada palabra por mayúscula.
Dejará el resto de la palabra intacta, ya sean números, símbolos, minúsculas o mayúsculas.
Finalmente retorna la cadena modificada.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/07"

import sys
import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def first_mayus(text: str) -> str:
    """Pasa la cadena caracter por caracter y cambia la primer letra de cada palabra por mayúscula.

    Si la primer letra de cada palabra es minúscula la volvera mayúscula, y si ya era mayúscula
    o si es otro tipo de caracter (como números o símbolos) simplemente ignora el caracter.

    Args:
        text (str): Cadena de texto a capitalizar.

    Raises:
        TypeError: Si recibe un argumento que no es una cadena.

    Returns:
        str: Cadena modificada con inciales en mayúscula.
    """

    if not isinstance(text, str):
        raise TypeError("Se requiere una cadena como argumento.")

    difference = ord('a') - ord('A')

    capitalized_text = ""
    is_first_letter = True

    for c in text:
        letter = c

        if is_first_letter and c.isalpha() and c.islower():
            letter = chr(ord(c) - difference)

        capitalized_text += letter
        is_first_letter = False

        if c == " " or c == "\t" or c == "\n":
            is_first_letter = True

    return capitalized_text

def _main():
    """Demo del programa. Ejecución principal"""

    _clear_console()

    if len(sys.argv) > 2:
        print("Se esperaba exactamente una cadena de texto!")
        _enter_to_continue()
        return

    print("-" * 20)
    print("En Mayúscula")
    print("-" * 20)

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        try:
            text = input("Ingresa el texto: ")
        except KeyboardInterrupt:
            print("\nPrograma cancelado por el usuario.")
            return

    try:
        print(
                f"Texto original: '{text}' "
                f"Texto modificado: '{first_mayus(text)}'\n"
            )
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    finally:
        input("Presiona Enter para continuar...")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
