"""Módulo para realizar las pruebas unitarias del módulo iteration_master.py.
Utiliza assert para verificar el funcionamiento esperado del módulo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os
import io
from contextlib import redirect_stdout
from colorama import Fore, Style, init
import iteration_master as im

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_iteradores_salida_correcta():
    """Verifica que los métodos de iteración impriman la secuencia exacta."""

    print(
        f"{Fore.YELLOW}{Style.BRIGHT}"
        "Ejecutando pruebas de salida a consola para "
        "las funciones del módulo iteration_master.py..."
    )

    #pylint: disable=protected-access
    secuencia_esperada = "".join(str(i) + im._get_sep(i) for i in range(im.MIN, im.MAX + 1))

    # Lista con las funciones que queremos evaluar
    metodos_a_probar = [
        im.iteration_for,
        im.iteration_while,
        im.iteration_recursive,
        im.iteration_list,
        im.iteration_stdlib,
        im.iteration_class,
        im.iteration_exec,
        im.iteration_eval,
    ]

    for metodo in metodos_a_probar:
        # Creamos un búfer de texto en memoria temporal
        bufer_memoria = io.StringIO()

        # Interceptamos el print() del método y lo desviamos a nuestro búfer
        with redirect_stdout(bufer_memoria):
            metodo()

        # Extraemos el texto capturado
        salida_consola = bufer_memoria.getvalue()

        # Verificamos que la salida contenga el nombre del método y la secuencia exacta
        assert secuencia_esperada in salida_consola, f"Falló el {metodo.__name__}"

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Impresión de resultados esperados.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*100}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_iteradores_salida_correcta()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente.")
    except AssertionError as err:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron: {err}")
    finally:
        print(f"{Fore.CYAN}{'='*100}")
