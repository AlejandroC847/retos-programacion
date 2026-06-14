"""
Módulo para realizar las pruebas del módulo conversor_tiempo.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/11"

import os
from pytest import raises, fail
from colorama import Fore, Style, init
import conversor_tiempo as ct

init(autoreset=True)

def _clear_console():
    """Limpia la consola de comandos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_convert_time():
    """Ejecuta pruebas para verificar la conversión de unidades de tiempo."""
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de conversión en 'convert_time()'...")

    # Valores por defecto (Todo en 0 -> 0 ms)
    assert ct.convert_time() == 0

    # Unidades Individuales
        # Solo segundos (1 segundo = 1,000 ms)
    assert ct.convert_time(secs=1) == 1000
    assert ct.convert_time(secs=15) == 15000
        # Solo minutos (1 minuto = 60,000 ms)
    assert ct.convert_time(mins=1) == 60000
    assert ct.convert_time(mins=5) == 300000
        # Solo horas (1 hora = 3,600,000 ms)
    assert ct.convert_time(hours=1) == 3600000
    assert ct.convert_time(hours=2) == 7200000
        # Solo días (1 día = 86,400,000 ms)
    assert ct.convert_time(days=1) == 86400000

    # Unidades Combinadas
        # Combinación estándar (1 min y 30 seg)
    # (1 * 60,000) + (30 * 1,000) = 90,000 ms
    assert ct.convert_time(mins=1, secs=30) == 90000
        # Combinación completa (1 día, 2 horas, 30 minutos y 15 segundos)
        # 86,400,000 + 7,200,000 + 1,800,000 + 15,000 = 95,415,000 ms
    assert ct.convert_time(days=1, hours=2, mins=30, secs=15) == 95415000

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Conversiones de unidades de tiempo esperadas...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las excepciones de tipo (TypeError)
    cuando se pasan argumentos que no son enteros.
    """
    print(f"{Fore.YELLOW}{Style.BRIGHT}Ejecutando pruebas de manejo de errores (TypeError)...")

    # Casos de tipos de datos incorrectos para el contenedor principal
    casos_invalidos_tipo = [4.5, "10", True, [1, 2], {"segundos": 5}, None]

    for caso in casos_invalidos_tipo:
        # Probando en el argumento 'days'
        with raises(TypeError):
            ct.convert_time(days=caso)

        # Probando en el argumento 'hours'
        with raises(TypeError):
            ct.convert_time(hours=caso)

        # Probando en el argumento 'mins'
        with raises(TypeError):
            ct.convert_time(mins=caso)

        # Probando en el argumento 'secs'
        with raises(TypeError):
            ct.convert_time(secs=caso)

    print(f"{Fore.GREEN}{Style.BRIGHT}\t✅ Pruebas de manejo de errores completadas con éxito.")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    try:
        _clear_console()
        print(f"{Fore.CYAN}{'='*40}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_convert_time()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except (AssertionError, fail.Exception):
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
    finally:
        print(f"{Fore.CYAN}{'='*40}")
