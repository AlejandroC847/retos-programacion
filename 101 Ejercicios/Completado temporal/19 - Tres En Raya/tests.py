"""
Módulo para realizar las pruebas del módulo tres_en_raya.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/11"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import tres_en_raya as ter

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_is_valid_board_content():
    """Ejecuta pruebas para la validación de los caracteres permitidos en el tablero."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_valid_board_content()'...")

    # Contenidos válidos estándar
    assert ter.is_valid_board_content((("X", "O", "X"), ("O", "X", ""), ("X", "", "O")))
    assert ter.is_valid_board_content((("", "", ""), ("", "", ""), ("", "", "")))

    # Contenido inválido por caracteres prohibidos (Debe retornar False)
    assert not ter.is_valid_board_content((("X", "O", "Z"), ("O", "X", ""), ("X", "", "O")))
    assert not ter.is_valid_board_content((("X", "4", "X"), ("O", "X", ""), ("X", "", "O")))
    assert not ter.is_valid_board_content((("X", "O", "X"), ("O", " ", ""), ("X", "", "O")))

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de validaciones de contenido esperados...")

def test_is_fair_game():
    """Ejecuta pruebas para la validación de la simetría y justicia de turnos."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'is_fair_game()'...")

    # Proporciones de turnos justas (Diferencia de X y O es <= 1)
    assert ter.is_fair_game((("X", "O", "X"), ("O", "X", ""), ("X", "", "O")))
    assert ter.is_fair_game((("", "", ""), ("", "", ""), ("", "", "")))

    # Proporciones de turnos injustas (Debe retornar False)
    assert not ter.is_fair_game((("X", "X", "X"), ("X", "", ""), ("", "O", "O")))
    assert not ter.is_fair_game((("O", "O", ""), ("O", "X", ""), ("", "", "")))
    assert not ter.is_fair_game((("X", "X", "X"), ("X", "X", ""), ("X", "X", "O")))

    print(
        f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Resultados de validaciones de justicia de juego esperados..."
    )

def test_evaluate_tic_tac_toe():
    """Ejecuta pruebas de integración sobre los resultados lógicos del juego."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'evaluate_tic_tac_toe()'...")

    # Caso 1: Ganador X en diagonal
    board_x = (("X", "O", "X"), ("O", "X", ""), ("X", "", "O"))
    assert ter.evaluate_tic_tac_toe(board_x) == "El ganador es el jugador con 'X'"

    # Caso 2: Ganador O en columna
    board_o = (("O", "X", "X"), ("O", "", ""), ("O", "X", ""))
    assert ter.evaluate_tic_tac_toe(board_o) == "El ganador es el jugador con 'O'"

    # Caso 3: Juego Nulo por movimientos injustos
    board_unfair = (("X", "X", "X"), ("X", "", ""), ("", "O", "O"))
    assert ter.evaluate_tic_tac_toe(board_unfair) == "Juego Nulo"

    # Caso 4: Juego Nulo por múltiples ganadores simultáneos
    board_multi = (("X", "X", "X"), ("O", "O", "O"), ("", "", ""))
    assert ter.evaluate_tic_tac_toe(board_multi) == "Juego Nulo"

    # Caso 5: Juego no terminado (movimientos legales, quedan vacíos, nadie gana)
    board_incomplete = (("X", "O", ""), ("", "X", "O"), ("O", "", ""))
    assert ter.evaluate_tic_tac_toe(board_incomplete) == "Juego no terminado!"

    # Caso 6: Empate (Tablero lleno sin ganadores)
    board_draw = (("X", "O", "X"), ("X", "O", "O"), ("O", "X", "X"))
    assert ter.evaluate_tic_tac_toe(board_draw) == "Empate"

    print(
        f"{Fore.GREEN}{Style.BRIGHT}\t"
        "✅ Simulación y resultados (evaluate_tic_tac_toe) aprobados..."
    )

def test_errores():
    """
    Verifica que el sistema maneje correctamente las excepciones de
    estructuras inválidas y dimensiones incorrectas.
    """
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores (Excepciones)...")

    # Casos de tipos de datos incorrectos para el contenedor principal
    casos_invalidos_tipo = [9.81, 847, True, {"matriz": "X"}, [3, 4, 5], None]

    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            ter.evaluate_tic_tac_toe(caso)
        with raises(TypeError):
            ter.is_valid_board_content(caso)
        with raises(TypeError):
            ter.is_fair_game(caso)

    # Estructuras internas incorrectas (Se esperan TypeError de subestructuras o celdas)
    with raises(TypeError):
        ter.evaluate_tic_tac_toe((("X", "", ""), ["", "O", ""], ("", "", "O")))   # Fila es lista
    with raises(TypeError):
        ter.evaluate_tic_tac_toe((("X", "O", "X"), ("O", 1, ""), ("X", "", "O"))) # Celda es entero

    # Geometrías incorrectas (Se esperan ValueError de dimensiones)
        # Falta una fila (solo tiene 2)
    with raises(ValueError):
        ter.evaluate_tic_tac_toe((("X", "", ""), ("", "O", "")))
        # Fila de 4 elementos
    with raises(ValueError):
        ter.evaluate_tic_tac_toe((("X", "O", "X", "O"), ("", "O", ""), ("", "", "O")))

    # Contenido ilegal que debe romper en la función principal
    with raises(ValueError):
        ter.evaluate_tic_tac_toe((("X", "O", "Z"), ("O", "X", ""), ("X", "", "O")))

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_is_valid_board_content()
        test_is_fair_game()
        test_evaluate_tic_tac_toe()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
