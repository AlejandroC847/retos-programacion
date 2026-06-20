"""Módulo para demostrar conceptos básicos de Python: sintaxis, variables, tipos de datos y salida.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/15"

import os

#pylint: disable=pointless-string-statement
#pylint: disable=invalid-name
#pylint: disable=unused-variable

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def introduccion():
    """Muestra los conceptos básicos de sintaxis, variables y tipos de datos en Python."""

    #Requisito 1: Crear un comentario...
    # Sitio oficial de Python: https://www.python.org
    # Este es un comentario de una linea

    """
    Este
    es
    un
    comentario
    multilinea"""


    # El lenguaje no soporta constantes pero se representan asi:
    CONSTANTE = 1   # noqa: F841

    # Las variables son de tipado dinámico
        # Entero
    entero = 1  # noqa: F841
        # Flotante
    flotante = 1.1  # noqa: F841
        # Complejo
    complejo = 3 + 5j #noqa: F841
        # print(complejo.real)  # Salida: 3.0
        # print(complejo.imag)  # Salida: 5.0

        # Booleano
    booleano = True # noqa: F841
        # String
    string = "Cadena"   # noqa: F841
        # Vacío o NoneType
    nulo = None # noqa: F841

    print("¡Hola, Python!")


def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 01 - Sintaxis, Variables, Tipos de Datos y Hola Mundo")
    print("-" * 20)

    introduccion() # Solo dice hola

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
