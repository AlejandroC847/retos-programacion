"""Módulo para realizar cálculos matemáticos a partir de un archivo de texto.
Lee un archivo .txt donde cada línea contiene un número o un operador,
y resuelve la operación de forma secuencial.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/13"

import os
from pathlib import Path
import sys

class ErrorDesconocido(Exception):
    """Excepción lanzada cuando la expresión de la calculadora tiene un formato corrupto."""
    def __init__(self, mensaje: str):
        # Pasamos el mensaje a la clase padre (Exception)
        super().__init__(mensaje)

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def calc_txt(file_name: str) -> tuple[str, int | float]:
    """Lee un archivo de texto y realiza las operaciones matemáticas contenidas en él.

    El archivo debe tener un formato donde cada línea sea un número o un operador
    (+, -, *, /). La función procesa la expresión de forma secuencial (de izquierda a derecha).

    Args:
        file_name (str): El nombre del archivo .txt a procesar.

    Returns:
        tuple[str, int | float]: Una tupla que contiene la expresión completa como string
        y el resultado numérico final.

    Raises:
        ValueError: Si en la expresión hay división por cero.
        ErrorDesconocido: Si se genera un error inesperado al validar.
        """

    lines = read_file(file_name)

    expression_str = " ".join(lines)

    if not validate_expression(expression_str):
        raise ErrorDesconocido("Se genero un error inesperado")
    elements = expression_str.split()

    result = float(elements[0])
    next_operator = ""

    for i, token in enumerate(elements):
        if i == 0:
            continue
        if i % 2 == 0:
            match next_operator:
                case "+":
                    result += float(token)
                case "-":
                    result -= float(token)
                case "*":
                    result *= float(token)
                case "/":
                    try:
                        result /= float(token)
                    except ZeroDivisionError as exc:
                        raise ValueError("No se puede dividir sobre cero.") from exc
        else:
            next_operator = token

    return (expression_str, result)

def validate_expression(expression: str) -> bool:
    """Valida que la expresión contenida en el archivo tenga un formato correcto.
    
    Debe seguir una estructura de: número operador número operador número...
    Los operadores permitidos son +, -, *, /.
    """

    if not isinstance(expression, str):
        raise TypeError("La expresión debe ser una cadena de texto.")

    list_expression = expression.split()

    if not list_expression:
        raise ValueError("La expresión está vacía.")

    numbers = list_expression[::2]
    operators = list_expression[1::2]

    for item in numbers:
        try:
            float(item)
        except ValueError as exc:
            raise ValueError(
                f"Carácter no permitido en la expresión."
                f"Se esperaba un número en la posición correspondiente pero se recibió: '{item}'."
            ) from exc

    for item in operators:
        if item not in ("+", "-", "/", "*"):
            raise ValueError(
                "Carácter no permitido en la expresión. Se esperaba un operador "
                f"('+', '-', '*' o '/') en la posición correspondiente pero se recibió: '{item}'."
            )

    if len(list_expression) % 2 == 0:
        raise ValueError("La expresión está incompleta. No puede terminar en un operador.")

    return True

def read_file(file_name: str) -> list[str]:
    """Lee el contenido de un archivo de texto y devuelve sus líneas.

    Args:
        file_name (str): El nombre del archivo a leer.

    Returns:
        list[str]: Una lista con las líneas del archivo.

    Raises:
        TypeError: Si el nombre del archivo no es un string.
        FileNotFoundError: Si el archivo no se encuentra en el directorio actual.
        """
    if not isinstance(file_name, str):
        raise TypeError("El nombre del archivo debe ser una cadena de texto.")

    actual_folder = Path(__file__).resolve().parent
    file_root = actual_folder / file_name

    if not file_root.exists():
        raise FileNotFoundError(f"El archivo '{file_name}' no existe dentro de {actual_folder}.")

    with open(file_root, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def write_file(file_name: str, list_text: list[str]):
    """Escribe una lista de cadenas de texto en un archivo, cada una en una línea nueva.

    Args:
        file_name (str): El nombre del archivo donde se escribirá.
        list_text (list[str]): Lista de cadenas de texto a escribir.

    Raises:
        TypeError: Si el nombre del archivo no es un string o list_text no es una lista.
        ValueError: Si algún elemento de la lista no es una cadena de texto.
        """
    if not isinstance(file_name, str):
        raise TypeError("El nombre del archivo debe ser una cadena de texto.")

    if not isinstance(list_text, list):
        raise TypeError("El contenido a escribir debe ser una lista de cadenas de texto.")

    for element in list_text:
        if not isinstance(element, str):
            raise TypeError("Todos los elementos de la lista deben ser cadenas de texto.")

    actual_folder = Path(__file__).resolve().parent
    file_root = actual_folder / file_name

    with open(file_root, "w", encoding="utf-8") as file:
        for text in list_text:
            file.write(f"{text}\n")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Calculadora .TXT")
    print("-" * 20)

    file = "entradas_calculadora.txt"

    if len(sys.argv) > 1:
        print("Escribiendo en disco la expresion...")
        write_file(file, sys.argv[1:])
    else:
        option = input("\n1. Escribir expresión\n2. Usar expresión existente\n> ")

        match option:
            case "1":
                user_expression = input(
                    "Ingrese la expresion matemática.\n"
                    "Solo se permiten números reales y operadores basicos (+, -, *, /) "
                    "separados por espacios. Ejemplo: '5 + 3 - 1 * 2 / 4'\n>"
                )

                write_file(file, user_expression.split())

            case "2":
                print("Recuperando datos locales...")
            case _:
                print("Opción Incorrecta!. Saliendo del programa...")
                _enter_to_continue()
                return

    try:
        expression, result = calc_txt(file)
        print(f"Expresion:\n{expression} = {result}")
    except (TypeError, ValueError, FileNotFoundError, ErrorDesconocido) as err:
        print(err)
    finally:
        _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
