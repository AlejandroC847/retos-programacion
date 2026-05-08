"""Crea una función que reciba dos cadenas como parámetros (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
    estén presentes en la str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
    estén presentes en la str1.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/05/06"

import sys
import os

def _limpiar_pantalla():
    """Limpia la consola de comandos dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def eliminar_caracteres(str1 : str, str2: str) -> tuple[str, str]:
    """Compara dos cadenas de texto y genera dos nuevas cadenas con los 
    caracteres únicos y ordenados alfabéticamente que no se comparten.
    - out1: Caracteres únicos presentes en str1 que NO están en str2.
    - out2: Caracteres únicos presentes en str2 que NO están en str1.
    
    Args:
        str1 (str): Primer cadena de texto.
        str2 (str): Segunda cadena de texto.

    Raises:
        TypeError: Si las entradas no son cadenas de texto.
    """

    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Las entradas deben ser cadenas de texto")

    str1 = str1.lower()
    str2 = str2.lower()

    str1_set = set(str1)
    str2_set = set(str2)

    out1 = "".join(sorted(str1_set - str2_set))
    out2 = "".join(sorted(str2_set - str1_set))

    return out1, out2

def filtrar_caracteres(str1 : str, str2: str) -> tuple[str, str]:
    """Compara dos cadenas de texto y genera dos nuevas cadenas manteniendo 
    el orden y los duplicados originales, pero eliminando los caracteres prohibidos.
    - out1: Cadena str1 tras eliminarle todos los caracteres que aparecen en str2.
    - out2: Cadena str2 tras eliminarle todos los caracteres que aparecen en str1.
    
    Args:
        str1 (str): Primer cadena de texto.
        str2 (str): Segunda cadena de texto.

    Raises:
        TypeError: Si las entradas no son cadenas de texto.
    """

    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Las entradas deben ser cadenas de texto")

    str1 = str1.lower()
    str2 = str2.lower()

    str1_set = set(str1)
    str2_set = set(str2)

    out1 = "".join(c for c in str1 if c not in str2_set)
    out2 = "".join(c for c in str2 if c not in str1_set)

    return out1, out2

def _main():
    # Demo del programa

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Error: Se requieren exactamente dos cadenas como argumentos.")
        return

    if len(sys.argv) > 1:
        print("-" * 20)
        print("MODO COMPARACIÓN RÁPIDA")
        print("-" * 20)

        print("\n[1] Caracteres únicos (Ordenados):")
        res_e = eliminar_caracteres(sys.argv[1], sys.argv[2])
        print(f"Cadena 1:{res_e[0]}")
        print(f"Cadena 2:{res_e[1]}")

        print("\n[2] Filtrado de texto (Orden original):")
        res_f = filtrar_caracteres(sys.argv[1], sys.argv[2])
        print(f"Cadena 1:{res_f[0]}")
        print(f"Cadena 2:{res_f[1]}")
    else:
        while True:
            _limpiar_pantalla()
            print("=" * 30)
            print("ELIMINANDO CARACTERES")
            print("Que operacion deseas hacer?")
            print("1. Filtrar Caracteres")
            print("\tCompara dos cadenas de texto y genera dos nuevas cadenas manteniendo"
                    " el orden y los duplicados originales, pero eliminando los "
                    "caracteres prohibidos.")
            print("2. Eliminar caracteres")
            print("\tCompara dos cadenas de texto y genera dos nuevas cadenas con los caracteres"
                    "únicos y ordenados alfabéticamente que no se comparten.")
            print("3. Salir")
            print("=" * 30)

            match input("Selecciona una opción: "):
                case "1":
                    s1 = input("Introduce la primera cadena: ")
                    s2 = input("Introduce la segunda cadena: ")
                    res = filtrar_caracteres(s1, s2)
                    print(f"Cadena 1:{res[0]}")
                    print(f"Cadena 2:{res[1]}")
                case "2":
                    s1 = input("Introduce la primera cadena: ")
                    s2 = input("Introduce la segunda cadena: ")
                    res = eliminar_caracteres(s1, s2)
                    print(f"Cadena 1:{res[0]}")
                    print(f"Cadena 2:{res[1]}")
                case "3":
                    print("Saliendo... Gracias por usar...\n")
                case _:
                    print("Respuesta incorrecta, intenta de nuevo...")
                    input("Presiona Enter para continuar...")
                    continue
            input("Presiona Enter para continuar...")
            break


# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    _main()
