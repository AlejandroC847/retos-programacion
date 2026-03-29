"""
Determina si dos cadenas de texto forman un anagrama.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial
aplicando reglas de reorganización:
    1. Reordenación Real: Dos palabras idénticas NO se consideran anagramas.
    2. Composición: Deben tener la misma frecuencia de cada carácter.
    3. Validación: No se requiere que las palabras pertenezcan a un diccionario.
    4. Normalización: La comparación ignora mayúsculas y minúsculas.
    5. Variación: Una cadena puede ser una frase mientras que la otra puede ser solo una palabra.
    6. Espaciado: Dos cadenas son diferentes si tienen diferentes cantidades de espacios o en
    diferentes posiciones a menos que los espacios se encuentren a los extremos o haya espacios
    multiples entre palabras; sin embargo, al evaluar ambas cadenas normalizadas, los espacios
    se ignorarán.
    6. Puntuación: Por fines practicos y no necesariamente semánticos, tambien se cuentan
    los signos de puntuación para un anagrama.
"""
__author__ = "Alejandro Cortés"
__date__ = "26/03/27"

from colorama import Fore, Style, init

init(autoreset=True)

# Formato de texto
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RED = Fore.RED
NORMAL = Style.NORMAL
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

# Estatus de evaluacion
STATUS_OK = "Es un anagrama"
STATUS_FAILED = "NO es un anagrama"
DIFF_LEN = "Diferente longitud! Cadenas inválidas!"
SAME_STR = "Es la misma cadena, NO es un anagrama."

def is_anagram(word_1: str, word_2: str) -> tuple[bool, str]:
    """
        Determina si una cadena es anagrama de otra siguiendo las reglas del módulo.
    Args:
        word_1 (str): Primera cadena a evaluar.
        word_2 (str): Segunda cadena a evaluar.

    Returns:
        tuple[bool, str]: Tupla con el resultado lógico y estatus de la evaluación.
    """

    # Todas minusculas
    w1_lower = word_1.lower()
    w2_lower = word_2.lower()

    # Normalización de espacios
    w1_normalized = " ".join(w1_lower.split())
    w2_normalized = " ".join(w2_lower.split())

    # Cadenas iguales no son anagrama
    if w1_normalized == w2_normalized:
        return (False, SAME_STR)

    # Eliminar espacios
    w1_clean = w1_normalized.replace(" ", "")
    w2_clean = w2_normalized.replace(" ", "")

    # Cadenas de diferente longitud no pueden ser anagramas
    if len(w1_clean) != len(w2_clean):
        return (False, DIFF_LEN)

    # Validación de anagrama
    if sorted(w1_clean) != sorted(w2_clean):
        return (False, STATUS_FAILED)

    # Es un anagrama
    return (True, STATUS_OK)

def evalue_anagram():
    """ Solicita la entrada de texto al usuario para recibir las dos cadenas y ejecuta
    la función is_anagram() para obtener el resultado lógico, imprimiendolo en patanlla."""

    #Limpia consola y muestra titulo
    print(f"\033[H\033[2J{CYAN}{BRIGHT}ES UN ANAGRAMA??\n{RESET}")

    w1 = input(f"{BRIGHT}Ingrese la primera cadena: ")
    w2 = input(f"{BRIGHT}Ingrese la Segunda cadena: ")

    print("Evaluando...")
    evaluacion, status = is_anagram(w1, w2)

    color = GREEN + BRIGHT if evaluacion else RED + NORMAL
    print(f"{color}{status}{RESET}")

# =========================
# Ejecución principal
# =========================

if __name__ == "__main__":
    evalue_anagram()
