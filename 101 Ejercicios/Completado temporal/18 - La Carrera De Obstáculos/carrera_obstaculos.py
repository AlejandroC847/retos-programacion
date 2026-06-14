"""Módulo para simular una carrera de obstáculos.
El programa evalúa si un atleta completa una pista basándose en una serie de acciones.
Las acciones permitidas son 'run' (correr) y 'jump' (saltar).
La pista se compone de '_' (suelo) y '|' (valla).
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/08"

import sys
import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def start_race(actions: list[str], track: str) -> bool:
    """Lorem Ipsum"""

    if not validate_actions(actions):
        raise ValueError(
            "Las acciones introducidas no son validas. Solo pueden ser 'run' o 'jump'."
        )
    if not validate_track(track):
        raise ValueError(
            "La pista introducida no es válida. Solo puede contener suelo('_') y vallas ('|')"
        )

    track_result = ""
    is_perfect_run = False

    obstacle_status = {
        "_": "run",
        "|": "jump"
    }

    for action, obstacle in zip(actions, track):
        if obstacle_status[obstacle] == action:
            track_result += "/"
        else:
            track_result += "x"

    if len(actions) >= len(track):
        is_perfect_run = all(s == "/" for s in track_result)
    else:
        is_perfect_run = False
        miss = len(track) - len(track_result)
        track_result += "x" * miss

    print_race_summary(track_result)

    return is_perfect_run

def validate_actions(actions: list[str]) -> bool:
    """Verifica que las acciones proporcionadas sean válidas (una lista de 'run' o 'jump').
    
    Args:
        actions (list[str]): Lista de acciones del atleta.

    Returns:
        bool: True si todas las acciones son válidas, False de lo contrario.

    Raises:
        TypeError: Si la entrada no es una lista o contiene elementos que no son cadenas de texto.
        """

    if not isinstance(actions, list):
        raise TypeError(
            f"Se esperaba una lista, pero se recibió un objeto de tipo '{type(actions).__name__}'."
        )
    for a in actions:
        if not isinstance(a, str):
            raise TypeError(f"La acción '{a}' no es una cadena de texto válida.")
        if a != "run" and a != "jump":
            return False
    return True

def validate_track(track: str) -> bool:
    """Verifica que la pista proporcionada sea válida (una cadena compuesta por '_' o '|').

    Args:
        track (str): Cadena de texto que representa la pista de obstáculos.

    Returns:
        bool: True si la pista contiene solo caracteres válidos, False de lo contrario.

    Raises:
        TypeError: Si la entrada no es una cadena de texto.
        """

    if not isinstance(track, str):
        raise TypeError(
            "Se esperaba una cadena de texto (str) para la pista, "
            f"pero se recibió un '{type(track).__name__}'."
            )
    # Sustituye al for. Retorna True si todos los elementos cumplen la condicion
    return all(obs == "|" or obs == "_" for obs in track)

def print_race_summary(result: str = ""):
    """Muestra un resumen de los resultados de la carrera en la consola.

    Args:
        result (str): Cadena de texto que representa el resultado de
        la carrera ('/' para acierto, 'x' para fallo).

    Raises:
        ValueError: Si el argumento proporcionado no es una cadena de texto.
    """

    if not isinstance(result, str):
        raise TypeError(
            "Se esperaba una cadena de texto (str) para el resultado, "
            f"pero se recibió un '{type(result).__name__}'."
        )

    print(f"Resultado de la carrera: {result}")

    misses = result.count("x")
    hits= result.count("/")

    if not misses or not result:
        print("Carrera terminada a la perfeccion!")
        return

    if not hits:
        print("Que desastre! No acertaste ninguna...")
        return

    print(
        "Tuviste:\n"
        f"\t{hits} aciertos.\n"
        f"\t{misses} errores.\n"
    )

def _main():
    """Demo del programa. Ejecución principal"""

    _clear_console()
    print("-" * 20)
    print("La Carrera De Obstáculos")
    print("-" * 20)

    if len(sys.argv) >= 3:
        track = sys.argv[1]
        #Crea la lista desde el argumento 3 en adelante.
        actions = list(sys.argv[2:])
    else:
        if len(sys.argv) == 2:
            print(
                "Se esperaban al menos 2 argumentos (pista y acciones)!. "
                "Pasando al registro manual...\n\n"
            )
            _enter_to_continue()

        try:
            track = ""
            actions = []
            while True:
                _clear_console()
                print("-" * 20)
                print("La Carrera De Obstáculos")
                print("-" * 20)

                if not track:
                    print("\tPista\nSolo se permite un texto plano con los"
                        "caracteres '_' (suelo) y '|' (valla) para la pista de obstáculos.\n"
                        "Ejemplo: '__|_|___|__'\n> "
                    )
                    track = input("Ingresa la pista: ")

                    if not all(obs == '_' or obs == '|' for obs in track):
                        print("La pista no es válida!!. Ingresela de nuevo..\n")
                        track =""
                        _enter_to_continue()
                        continue

                print(
                    "\tAcciones \nLas acciones deberan ser 'run' o 'jump'. "
                    "Solo debes ingresar una a una las acciones y automaticamente se "
                    "registrarán para la carrera. Para terminar de agregar acciones escribe "
                    "'exit' (e) o 'salir' (s).\n")

                action = input("Ingresa la acción: ").lower()

                if action == "run" or action == "jump":
                    actions.append(action)
                elif action == "e" or action == "s" or action == "exit" or action == "salir":
                    print("Finalizando la adición de acciones...")
                    _enter_to_continue()
                    break
                else:
                    print(f"La acción {action} no es válida!")
                    _enter_to_continue()
        except KeyboardInterrupt:
            print("\nPrograma cancelado por el usuario.")
            return

    try:
        print(
            "Estado de la carrera: "
            f"{'Terminada' if start_race(actions, track) else 'NO terminada'}\n"
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
