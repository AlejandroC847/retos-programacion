"""Módulo que recibe un texto y retorna verdadero o falso (Boolean) 
según sean o no palíndromos.
Un palíndromo es una palabra o expresión que es igual si se lee de izquierda 
a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/07"

import sys
import os

def _clear_screen():
    # Limpia la consola de comandos
    os.system('cls' if os.name == 'nt' else 'clear')

def is_palindrome(string: str) -> bool:
    """Verifica si una cadena de texto es un palíndromo, ignorando mayúsculas, 
    acentos y caracteres no alfanuméricos.
    
    Args:
        string (str): La cadena de texto a evaluar.

    Raises:
        TypeError: Si la entrada no es una cadena de texto.

    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """

    if not isinstance(string, str):
        raise TypeError("La entrada debe ser una cadena de texto")

    string = string.lower()
    tabla = str.maketrans("áéíóú", "aeiou")
    string = string.translate(tabla)

    string = "".join(c for c in string if c.isalnum())

    for c in string:
        if not c.isalnum():
            string = string.replace(c, "")

    return string == string[::-1]

def _main():
    # Demo de programa
    _clear_screen()
    if len(sys.argv) > 2:
        print("Error: Se requiere exactamente una cadena como argumento.")
        return
    if len(sys.argv) > 1:
        print("-" * 20)
        print("Es un Palíndromo?")
        print("-" * 20)

        res = is_palindrome(sys.argv[1])
        print(f"La Cadena {sys.argv[1]} {'SI' if res else 'NO'} es un Palíndromo.")
    else:
        print("-" * 20)
        print("Es un Palíndromo?")
        print("-" * 20)

        string = input("Ingrese una cadena: ")

        res = is_palindrome(string)
        print(f"La Cadena {string} {'SI' if res else 'NO'} es un Palíndromo.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
