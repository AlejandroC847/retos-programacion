"""
Módulo para realizar las pruebas del módulo carrera_obstaculos.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/09"

import carrera_obstaculos as co
from pytest import raises, fail
from colorama import Fore, Style, init
import os

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_validate_track():
    """Ejecuta pruebas para la validación del formato de la pista."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'validate_track()'...")

    # Pistas válidas estándar
    assert co.validate_track("_")
    assert co.validate_track("|")
    assert co.validate_track("__|_|__")
    # Pista vacía
    assert co.validate_track("")
    # Pistas inválidas por caracteres no permitidos
    assert not co.validate_track(" ")
    assert not co.validate_track("2")
    assert not co.validate_track("__x__")
    assert not co.validate_track("hola")
    assert not co.validate_track("__|_|__-")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de validaciones esperados...")

def test_validate_actions():
    """Ejecuta pruebas para la validación de la lista de acciones."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'validate_actions()'...")

    # Acciones válidas estándar
    assert co.validate_actions(["run"])
    assert co.validate_actions(["jump"])
    assert co.validate_actions(["run", "run", "jump", "run"])
    # Lista vacía (Válido para el caso de carrera vacía)
    assert co.validate_actions([])
    # Acciones inválidas por cadenas incorrectas
    assert not co.validate_actions(["RUN"])
    assert not co.validate_actions(["run ", "jump"])
    assert not co.validate_actions(["swim"])
    assert not co.validate_actions(["run", "error", "jump"])

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Resultados de validaciones esperados...")

def test_start_race():
    """Ejecuta pruebas de integración sobre la simulación completa de la carrera."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de 'start_race()'...")

    # Caso 1: Carrera perfecta
    assert co.start_race(["run", "run", "jump", "run"], "__|_")
    # Caso 2: Más acciones de las necesarias pero perfectas
    assert co.start_race(["run", "run", "jump", "run", "run", "run"], "__|_")
    # Caso 3: Carrera vacía (Victoria automática)
    assert co.start_race([], "")
    # Caso 4: El atleta se equivoca de acciones (Carrera NO perfecta)
    assert not co.start_race(["run", "jump", "jump", "run"], "__|_")
    # Caso 5: Faltan acciones para completar el largo de la pista
    assert not co.start_race(["run", "run"], "__|_")

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Simulación de carreras (start_race) aprobada...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    casos_invalidos_tipo = [9.81, 847, True, {"pista": "_"}, [3, 4, 5], None]

    for caso in casos_invalidos_tipo:
        with raises(TypeError):
            co.validate_track(caso)
        with raises(TypeError):
            co.print_race_summary(caso)

        with raises(TypeError):
            co.validate_actions(caso)

    with raises(ValueError):
        co.start_race(["swim", "run"], "__|_")  # Acción inválida
    with raises(ValueError):
        co.start_race(["run", "jump"], "__X_")  # Pista inválida


    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_validate_track()
        test_validate_actions()
        test_start_race()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
