"""Crea un programa que reciba una expresión matemática y verifique si los
paréntesis, llaves y corchetes están equilibrados.
- Los signos de agrupación deben cerrarse en el orden correcto.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/05"

import sys

def is_balanced(expression: str) -> bool:
    """Verifica si una expresión matemática tiene sus signos de agrupación
    (paréntesis, llaves y corchetes) equilibrados y cerrados en el orden correcto.

    Args:
        expression (str): La cadena de texto que contiene la expresión a evaluar.

    Returns:
        bool: True si la expresión está equilibrada, False en caso contrario.

    Raises:
        TypeError: Si la entrada no es una cadena de texto.
    """

    if not isinstance(expression, str):
        raise TypeError("La entrada debe ser una cadena de texto")

    stack = []

    for c in expression:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack:
                return False
            opening = stack.pop()
            if  (c == ")" and opening != "(") or \
                (c == "]" and opening != "[") or \
                (c == "}" and opening != "{"):
                return False

    if stack:
        return False

    return True

def _main():
    # Función principal. Demo del programa.
    if len(sys.argv) > 1:
        entrada = "".join(sys.argv[1:])
        is_balanced(entrada)
    else:
        expression = input("Introduce la expresion: ")
        is_balanced(expression)

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
