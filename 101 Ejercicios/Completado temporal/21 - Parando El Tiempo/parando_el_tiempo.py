"""Módulo para realizar sumas asíncronas tras un tiempo de espera determinado.
Utiliza asyncio para manejar la concurrencia y permite configurar el retardo.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/12"

import os
import asyncio

MAX_TIMEOUT_SECONDS = 15

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

async def stop_time(
            a: int | float = 0,
            b: int | float = 0,
            await_time: int | float = 0
        ) -> int | float:
    """Suma dos números tras un tiempo de espera determinado.

    Args:
        a (int | float): Primer número a sumar.
        b (int | float): Segundo número a sumar.
        await_time (int | float): Tiempo de espera en segundos antes de realizar la suma.

    Returns:
        int | float: La suma de a + b.

    Raises:
        TypeError: Si alguno de los argumentos no es un número (int o float).
        ValueError: Si el tiempo es negativo o excede el límite de seguridad.
        """

    # region Validaciones de Tipo
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"El argumento 'a' debe ser numérico. Se recibió {type(a).__name__}")

    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"El argumento 'b' debe ser int o float. Se recibió {type(b).__name__}")

    if not isinstance(await_time, (int, float)) or isinstance(await_time, bool):
        raise TypeError(
            f"El argumento 'seconds' debe ser numérico. Se recibió {type(await_time).__name__}"
        )
    # endregion

    # region Validaciones de Valor
    if await_time < 0:
        raise ValueError(f"El tiempo de espera no puede ser negativo. Se recibió: {await_time}")

    if await_time > MAX_TIMEOUT_SECONDS:
        raise ValueError(
            f"El tiempo de espera excede el límite permitido de {MAX_TIMEOUT_SECONDS} segundos."
            )
    # endregion

    await asyncio.sleep(await_time)

    print(
        f"> Suma de {a} + {b} en {await_time} seg...\n"
        f"\tEl resultado es = {a + b}"
    )

    return a + b



async def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Parando El Tiempo")
    print("-" * 20)

    try:
        suma1 = (5, 5, 6)
        suma2 = (10, 20, 2)
        suma3 = (1.5, 2.5, 3.5)

        task1 = asyncio.create_task(stop_time(*suma1))
        task2 = asyncio.create_task(stop_time(*suma2))
        task3 = asyncio.create_task(stop_time(*suma3))

        print("Sumas en proceso, continua la ejecución demo de forma asíncrona.")
        print("Esperando resultados...\n")

        res1 = await task1
        res2 = await task2
        res3 = await task3

        print(f"\n\n➡️ [Retorno Recibido] Resultado Suma 1: {suma1[0]} + {suma1[1]} = {res1}")
        print(f"➡️ [Retorno Recibido] Resultado Suma 2: {suma2[0]} + {suma2[1]} = {res2}")
        print(f"➡️ [Retorno Recibido] Resultado Suma 3: {suma3[0]} + {suma3[1]} = {res3}\n")

    except TypeError as te:
        print(te)
    finally:
        input("Presiona Enter para continuar...")

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    asyncio.run(_main())
