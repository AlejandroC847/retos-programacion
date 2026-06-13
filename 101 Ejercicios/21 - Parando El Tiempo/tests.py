"""Módulo para realizar las pruebas del módulo parando_el_tiempo.py.
Se utiliza assert y pytest para verificar que se obtienen
los resultados esperados de forma asíncrona.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/12"

import os
import asyncio
import time
from pytest import raises, fail
from colorama import Fore, Style, init
import parando_el_tiempo as pt

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_stop_time():
    """Ejecuta pruebas para verificar el flujo exitoso (Happy Path) de las sumas."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de flujo exitoso en 'stop_time()'...")

    # Valores por defecto (Todo en 0)
    # Como stop_time es async, usamos asyncio.run() para ejecutarla dentro del assert síncrono
    assert asyncio.run(pt.stop_time()) == 0

    # Sumas con Enteros (Happy Path)
    assert asyncio.run(pt.stop_time(5, 5, await_time=0.1)) == 10
    assert asyncio.run(pt.stop_time(10, 20, await_time=0)) == 30

    # Sumas con Flotantes (Happy Path)
    assert asyncio.run(pt.stop_time(1.5, 2.5, await_time=0.1)) == 4.0
    assert asyncio.run(pt.stop_time(0.5, 0.5, await_time=0)) == 1.0

    # Sumas de 5 segundos
    assert asyncio.run(pt.stop_time(await_time=5)) == 0

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Calculos de sumas esperados...")

def test_concurrencia():
    """Demuestra y verifica que las tareas realmente se ejecuten al mismo tiempo (en paralelo)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando prueba de concurrencia (Paralelismo)...")

    async def secuencia_paralela():
        # Creamos las tareas para que corran en el fondo simultáneamente
        task1 = asyncio.create_task(pt.stop_time(1, 1, await_time=1))
        task2 = asyncio.create_task(pt.stop_time(2, 2, await_time=1))
        task3 = asyncio.create_task(pt.stop_time(3, 3, await_time=1))
        # Recolectamos los resultados de golpe
        return await asyncio.gather(task1, task2, task3)

    inicio = time.perf_counter()
    resultados = asyncio.run(secuencia_paralela())
    tiempo_total = time.perf_counter() - inicio

    # Verificación de resultados de la suma
    assert resultados == [2, 4, 6]

    # Si fuera síncrono tardaría 3 segundos (1s + 1s + 1s).
    assert not tiempo_total > 3

    # Al ser asíncrono debe tardar un milisegundo extra sobre el segundo base o incluso menos.
    assert tiempo_total < 1.3

    print(
        f"{Fore.GREEN}{Style.BRIGHT}\t"
        f"✅ Concurrencia demostrada con éxito. Tiempo total: {tiempo_total:.4f}s"
    )

def test_errores():
    """Verifica que el sistema lance una excepción ante tipos de datos no válidos o
    booleanos (TypeError), o ante tiempos negativos o fuera del límite (ValueError)."""

    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores...")

    casos_invalidos_tipo = ("5", [1, 2], {"tiempo": 2}, None, True, False)
    casos_invalidos_valor = (-5, 10000)

    for caso in casos_invalidos_tipo:
        # Probando en el argumento 'a'
        with raises(TypeError):
            asyncio.run(pt.stop_time(a=caso, b=5, await_time=0))
        # Probando en el argumento 'b'
        with raises(TypeError):
            asyncio.run(pt.stop_time(a=5, b=caso, await_time=0))
        # Probando en el argumento 'await_time'
        with raises(TypeError):
            asyncio.run(pt.stop_time(a=5, b=5, await_time=caso))

    for caso in casos_invalidos_valor:
        with raises(ValueError):
            asyncio.run(pt.stop_time(5, 5, await_time=caso))

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        #test_stop_time()
        test_concurrencia()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
