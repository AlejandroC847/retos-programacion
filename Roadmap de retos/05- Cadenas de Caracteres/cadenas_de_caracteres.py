"""Módulo de muestra para el tipo de dato str:
- demo_str(): Muestra las operaciones disponibles para str.
- is_anagram(): Recibe dos cadenas y determina si son un anagrama.
- is_palindrome(): Recibe una cadena y determina si es un palíndromo.
- is_isogram(): Recibe una cadena y determina si es un isograma.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/19"

import os
import unicodedata

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

def demo_str():
    """String (str): Inmutables, permiten cualquier caracter unicode y los duplicados."""

    cadena = "Texto"

    # Transformación de formato
        # Estos métodos devuelven una versión modificada del texto.

    cadena.upper()              # Convierte todo a mayúsculas o minúsculas.
    cadena.lower()              # Convierte todo a mayúsculas o minúsculas.

    cadena.capitalize()         # Pone en mayúscula solo la primera letra.

    cadena.title()              # Pone en mayúscula la primera letra de cada palabra.

    cadena.strip()              # Elimina los espacios en blanco al inicio y al final
    cadena.lstrip()             # Elimina los espacios en blanco al inicio (izquierda)
    cadena.rstrip()             # Elimina espacios en blanco al final (derecha)
    # Por defecto quitan saltos de línea, tabulaciones, retornos de carro o espacios.
    # Pero se puede pasar una cadena como argumento para ahora eliminar el contenido.

    cadena.replace("to", "as")  # Reemplaza una subcadena por otra.

    # Búsqueda y Validación
        # Devuelven un booleano o un índice.

    cadena.find("s")            # Busca la posicion de una subcadena (-1 si no lo encuentra)
    cadena.index("x")           # (lanza error si no lo encuentra)

    cadena.startswith("t")      # Verifican si el string comienza o termina con un texto dado.
    cadena.endswith("o")        # Verifica si el string termina con un texto dado.

    cadena.isdigit()            # Valida si el contenido son solo números
    cadena.isalpha()            # Valida si el contenido son solo letras
    cadena.isalnum()            # Valida si el contenido son solo caracteres alfanuméricos

    # División y Unión

    cadena.split("/")           # Divide un string en una lista usando un separador
                                # (Por defecto es espacio)
    cadena.join(["A", "B", "C"])      # Une elementos de una lista en un solo string que
                                # retorna usando la cadena como separador o unión.

    print(f"Cadena final (demo): '{cadena}'")

def is_anagram(word_1: str, word_2: str) -> tuple[bool, str]:
    """
        Determina si una cadena es anagrama de otra siguiendo las reglas del módulo.
    Args:
        word_1 (str): Primera cadena a evaluar.
        word_2 (str): Segunda cadena a evaluar.

    Returns:
        tuple[bool, str]: Tupla con el resultado lógico y estatus de la evaluación.
    """

    if not isinstance(word_1, str):
        raise TypeError(
            "El primer argumento debe ser una cadena de texto."
            f"Se recibió {type(word_1).__name__}"
        )
    if not isinstance(word_2, str):
        raise TypeError(
            "El segundo argumento debe ser una cadena de texto."
            f"Se recibió {type(word_2).__name__}"
        )

    # Todas minusculas
    w1_lower = word_1.lower()
    w2_lower = word_2.lower()

    # Normalización de espacios
    w1_normalized = " ".join(w1_lower.split())
    w2_normalized = " ".join(w2_lower.split())

    # Cadenas iguales no son anagrama
    if w1_normalized == w2_normalized:
        return (False, "Es la misma cadena, NO son un anagrama.")

    # Eliminar espacios
    w1_clean = w1_normalized.replace(" ", "")
    w2_clean = w2_normalized.replace(" ", "")

    # Cadenas de diferente longitud no pueden ser anagramas
    if len(w1_clean) != len(w2_clean):
        return (False, "Diferente longitud! Cadenas inválidas!")

    # Validación de anagrama
    if sorted(w1_clean) != sorted(w2_clean):
        return (False, "NO son un anagrama")

    # Es un anagrama
    return (True, "SON un anagrama")

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

def is_isogram(string: str) -> bool:
    """Verifica si una cadena de texto es un isograma, ignorando mayúsculas, 
    acentos y caracteres no alfanuméricos.
    
    Args:
        string (str): La cadena de texto a evaluar.

    Raises:
        TypeError: Si la entrada no es una cadena de texto.

    Returns:
        bool: True si es isograma, False en caso contrario.
    """

    if not isinstance(string, str):
        raise TypeError("La entrada debe ser una cadena de texto")

    # Normalizar tildes y caracteres raros
    nfkd_form = unicodedata.normalize('NFKD', string.lower())
    sin_tildes = "".join([c for c in nfkd_form if not unicodedata.combining(c)])

    #Quitar simbolos y espacios
    limpio = "".join([c for c in sin_tildes if c.isalnum()])

    chars = set(limpio)

    return len(chars) == len(limpio)

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 05 - Cadenas de Caracteres")
    print("-" * 20)

    demo_str()

    print("\tAnagrama:")
    p1 = "Roma"
    p2 = "Amor"

    print(f"Las palabras demo son: {p1} y {p2}. {is_anagram(p1, p2)[1]}")

    print("\tPalíndromo")
    print(
        f"La palabra: {p1} {"ES un Palíndromo" if is_palindrome(p1) else "NO es un Palíndromo"}"
    )
    print(
        f"La palabra: {p2} {"ES un Palíndromo" if is_palindrome(p2) else "NO es un Palíndromo"}"
    )

    print("\tIsograma")
    print(
        f"La palabra: {p1} {"ES un Isograma" if is_isogram(p1) else "NO es un Isograma."}"
    )
    print(
        f"La palabra: {p2} {"ES un Isograma" if is_isogram(p2) else "NO es un Isograma."}"
    )

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
