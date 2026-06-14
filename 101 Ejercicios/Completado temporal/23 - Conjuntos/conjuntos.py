"""Módulo para realizar operaciones de conjuntos sobre listas.
Permite obtener la intersección o la diferencia simétrica entre dos colecciones
sin uso de operaciones del lenguaje que las resuman.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/14"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def sets(array_a: list = None, array_b: list = None, find_common: bool = True) -> list:
    """Encuentra elementos comunes o diferentes entre dos listas.

    Args:
        array_a (list, optional): Primera lista de elementos.
        array_b (list, optional): Segunda lista de elementos.
        find_common (bool, optional): Si es True, devuelve la intersección.
            Si es False, devuelve la diferencia simétrica. Por defecto es True.

    Returns:
        list: Lista con los elementos resultantes sin duplicados.

    Raises:
        TypeError: Si los argumentos no son del tipo esperado.
        """

    if array_a is None:
        array_a = []

    if array_b is None:
        array_b = []

    if not isinstance(array_a, list):
        raise TypeError(
            "El primer conjunto 'array_a'debe ser una lista. "
            f"Se recibió {type(array_a).__name__}"
        )

    if not isinstance(array_b, list):
        raise TypeError(
            "El segundo conjunto 'array_b'debe ser una lista. "
            f"Se recibió {type(array_b).__name__}"
        )

    if not isinstance(find_common, bool):
        raise TypeError(
            "La bandera para encontrar elementos comunes 'find_common' debe ser un booleano. "
            f"Se recibió {type(find_common).__name__}"
        )

    results = []

    if find_common:
        for e in array_a:
            if e in array_b and e not in results:
                results.append(e)
    else:
        for e in array_a:
            if e not in array_b and e not in results:
                results.append(e)
        for e in array_b:
            if e not in array_a and e not in results:
                results.append(e)

    return results

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Conjuntos")
    print("-" * 20)

    try:
        set_a = [1, 2, 3, 4, 5]
        set_b = [3, 4, 5, 6, 7]

        inter = sets(set_a, set_b)
        diff = sets(set_a, set_b, False)

        print(
            f"A = {{{', '.join(str(x) for x in set_a)}}}\n"
            f"B = {{{', '.join(str(x) for x in set_b)}}}\n"
        )

        print(
            "Elementos en común: "
            f"{{{', '.join(str(x) for x in inter)}}}"
        )
        print(
            "Elementos no comunes: "
            f"{{{', '.join(str(x) for x in diff)}}}"
        )

    except TypeError as err:
        print(err)
    finally:
        _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
