"""Módulo para evaluar el estado de una partida de Tres en Raya (Tic-Tac-Toe).
Permite determinar ganadores, empates, juegos no terminados o estados nulos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/10"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def evaluate_tic_tac_toe(game_matrix: tuple[
                            tuple[str, str, str],
                            tuple[str, str, str],
                            tuple[str, str, str]]
                        ) -> str:
    """Evalúa el estado de una partida de Tres en Raya (Tic-Tac-Toe).

    Analiza una matriz de 3x3 para determinar si hay un ganador ('X' o 'O'),
    si el juego ha terminado en empate, si aún está en curso o si el tablero
    es inválido (Juego Nulo) debido a movimientos injustos o múltiples ganadores.

    Args:
        game_matrix (tuple): Una tupla de 3 tuplas, donde cada una contiene 3 strings
                            que representan las filas del tablero ('X', 'O' o '').

    Returns:
        str: Un mensaje indicando el resultado:
            - "El ganador es el jugador con 'X'"
            - "El ganador es el jugador con 'O'"
            - "Empate"
            - "Juego no terminado!"
            - "Juego Nulo" (Si no es justo o hay contradicciones)

    Raises:
        ValueError: Si la matriz contiene caracteres no permitidos.
        TypeError: Si la estructura de la matriz no es una tupla de tuplas de strings.
        """

    if not is_valid_board_content(game_matrix):
        raise ValueError(
            "La matriz contiene caracteres no válidos. "
            "Solo se permiten 'X', 'O' o cadenas vacías ''."
            )

    if not is_fair_game(game_matrix):
        return "Juego Nulo"

    flat = [cell for row in game_matrix for cell in row]

    matches_x = 0
    matches_o = 0

    possible_combinations = ( # Para matriz aplanada
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Columnas
        (0, 4, 8), (2, 4, 6)                # Diagonales
    )

    for c in possible_combinations:
        set_combination = {flat[c[0]], flat[c[1]], flat[c[2]]}

        if len(set_combination) == 1 and "" not in set_combination:
            ganador = next(iter(set_combination))
            matches_x += 1 if ganador == "X" else 0
            matches_o += 1 if ganador == "O" else 0

    #Verificar ganador

    if matches_x > 0 and matches_o > 0:
        return "Juego Nulo"

    if matches_x > 0:
        return "El ganador es el jugador con 'X'"
    if matches_o > 0:
        return "El ganador es el jugador con 'O'"

    if "" in flat:
        return "Juego no terminado!"

    return "Empate"

def is_valid_board_content(
    game_matrix: tuple[
        tuple[str, str, str],
        tuple[str, str, str],
        tuple[str, str, str]]
    ) -> bool:
    """Verifica que el contenido de la matriz de juego sea válido.
    Comprueba que cada casilla contenga únicamente 'X', 'O' o una cadena vacía.

    Args:
        game_matrix (tuple): Matriz de 3x3 que representa el tablero.

    Returns:
        bool: True si el contenido es válido, False en caso contrario.
    """

    _validate_board_structure(game_matrix)

    for row in game_matrix:
        for cell in row:
            if cell not in ("X", "O", ""):
                return False
    return True

def is_fair_game(
    game_matrix: tuple[
        tuple[str, str, str],
        tuple[str, str, str],
        tuple[str, str, str]]
    ) -> bool:
    """Verifica si el juego es justo basándose en la cantidad de movimientos.
    Un juego es justo si la diferencia entre el número de 'X' y 'O' es como máximo 1.

    Args:
        game_matrix (tuple): Matriz de 3x3 que representa el tablero.

    Returns:
        bool: True si el juego es justo, False en caso contrario.
    """
    _validate_board_structure(game_matrix)

    flat = [cell for row in game_matrix for cell in row]

    # Contamos cuántas X y O hay en total
    total_x = flat.count("X")
    total_o = flat.count("O")
    total_vacios = flat.count("")

    # Si la suma de X, O y vacíos no da 9, significa que hay caracteres extraños
    if (total_x + total_o + total_vacios) != 9:
        return False

    return abs(total_x - total_o) <= 1

def _validate_board_structure(game_matrix) -> None:
    """Verifica que la estructura de la matriz de juego sea válida.
    Comprueba que sea una tupla de 3x3 y que cada elemento sea una cadena de texto.

    Args:
        game_matrix: El objeto a validar.

    Raises:
        TypeError: Si la estructura o los tipos de datos no son los esperados.
        ValueError: Si las dimensiones de la matriz no son 3x3.
        """

    if not isinstance(game_matrix, tuple):
        raise TypeError(
            "Error: El contenedor principal de la matriz de juego debe ser una tupla."
            f"Se recibió un valor de tipo {type(game_matrix).__name__}"
            )

    if len(game_matrix) != 3:
        raise ValueError(
            "Error: La matriz de juego debe tener exactamente 3 filas. "
            f"Se recibieron {len(game_matrix)} filas."
            )

    for row in game_matrix:
        if not isinstance(row, tuple):
            raise TypeError(
                "Error: Cada fila de la matriz debe ser una tupla. "
                f"Se recibió un valor de tipo {type(row).__name__}"
            )
        if len(row) != 3:
            raise ValueError(
                "Error: Cada fila debe tener exactamente 3 casillas. "
                f"Se recibieron {len(row)} casillas."
                )
        for cell in row:
            if not isinstance(cell, str):
                raise TypeError(
                    "Error: Cada casilla del tablero debe ser una cadena de texto (str)."
                    f"Se recibió un valor de tipo {type(cell).__name__}"
                )

def print_game_matrix(game_matrix: tuple[
                        tuple[str, str, str],
                        tuple[str, str, str],
                        tuple[str, str, str]]
                    ) -> None:
    """Imprime de forma visual el tablero de Tres en Raya en la consola.

    Args:
        game_matrix (tuple): Matriz de 3x3 que representa el tablero.
    """

    print("Matriz de Juego:\n")
    print("┌───┬───┬───┐")
    for i, row in enumerate(game_matrix):
        row_format = [cell if cell != "" else " " for cell in row]
        print(f"│ {row_format[0]} │ {row_format[1]} │ {row_format[2]} │")

        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Tres En Raya")
    print("-" * 20)

    # Matriz de prueba
    game = (
        ("X", "O", "X"),
        ("O", "X", ""),
        ("X", "", "O"),
    )

    print_game_matrix(game)

    try:
        print(evaluate_tic_tac_toe(game))
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
