"""Módulo que justifica la inexistencia de asignación "por valor" y "por referencia" en Python.
Se explican los conceptos de inmutabilidad y mutabilidad de los tipos de datos,
asi como el funcionamiento básico de reserva de memoria al crear variables.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/20"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

def val_ref_intro():
    """Imprime en consola una explicación didáctica sobre el manejo de memoria en Python.

    Detalla las diferencias entre tipos de datos mutables e inmutables, explicando
    el comportamiento de asignación 'por valor' y 'por referencia'. Incluye
    ejemplos prácticos en consola que ilustran cómo se comportan las variables 
    al ser asignadas y modificadas.
    """

    print( #+ Introducción
        "En python todos los tipos de datos son objetos; por lo tanto, siempre que se\n"
        "asigna un valor a una variable se pasa la referencia del objeto.\n"
        "Sin embargo, la forma de representar los diferentes tipos de asignación se determina\n"
        "si se accede al mismo espacio en memoria (por referencia) o si se crea un nuevo espacio\n"
        "independiente (por valor). Para ello hay dos tipos de datos:"
    )
    print(#+ Datos inmutables
        "Inmutables (Pasan 'como por valor'):\n"
        "Cuando pasas un entero o un string a una función y lo modificas, en realidad estás\n"
        "creando un nuevo objeto en un nuevo espacio de memoria. La variable original fuera\n"
        "de la función no cambia."
    )
    print(#+ Datos mutables
        "Mutables (Pasan 'como por referencia'):\n"
        "Cuando pasas una lista o diccionario, pasas la referencia al objeto. Si modificas o\n"
        "agregas un índice dentro de la función, el objeto original sí cambia.\n"
    )

    # Inmutables
    print("\n\tTipos Inmutables:\n")
    print(
        "Los tipos de datos inmutables son los siguientes:\n"
        "- int (Enteros)\n"
        "- float (Números de punto flotante)\n"
        "- complex (Números complejos)\n"
        "- bool (Booleanos)\n"
        "- str (Cadenas de texto)\n"
        "- frozenset (Conjuntos inmutables)\n"
        "- tuple (Tuplas)\n"
        "- bytes (Secuencias de bytes)\n"
        "- NoneType (El valor None)\n"
    )
    print(
        "Al declararse el valor de un tipo inmutable se reserva un espacio en memoria.\n"
        "Si se crea otro objeto a partir del mismo valor pero siendo tambien inmutable\n"
        "se reserava otro espacio en memoria diferente para ese nuevo objeto (por Valor).\n"
    )
    print(
        "Ejemplo: Las cadenas\n"
        "\tstr1 = 'Hola'\n"
        "\tstr2 = str1\n"
        "\tstr2 = ''\n"
        "Aunque se modifique str2, str1 conserva el mismo valor porque es inmutable."
    )

    str1 = 'Hola'
    str2 = str1
    str2 = ''
    print(f"Valor final de str1: '{str1}'")
    print(f"Valor final de str2: '{str2}'")

    # Mutables
    print("\n\tTipos Mutables:\n")
    print(
        "Los tipos de datos mutables son los siguientes:\n"
        "- list (Listas)\n"
        "- set (Conjuntos)\n"
        "- dict (Diccionarios)\n"
        "- bytearray\n"
        "- collections.deque(Cola de doble extremo)\n"
    )
    print(
        "Al declararse el valor de un tipo mutable se reserva un espacio en memoria.\n"
        "Si se crea otro objeto a partir del mismo valor siendo de tipo mutable\n"
        "se le asigna la referencia al mismo espacio en memoria, por lo que cualquier\n"
        "modificación en un objeto se verá reflejada en el otro (Por referencia).\n"
        "Para evitar este comportamiento con los tipos mutables se necesita hacer explicita la\n"
        "creacion de un nuevo espacio en memoria (por ejemplo con constructoes como list())."
    )
    print(
        "Ejemplo: Las listas\n"
        "\tlista1 = [1, 2, 3]\n"
        "\tlista2 = lista1\n"
        "\tlista2.append(4)\n"
        "Al modificar la lista2 se reflejan los cambios en lista1 "
        "porque apuntan al mismo espacio de memoria."
    )

    lista1 = [1, 2, 3]
    lista2 = lista1
    lista2.append(4)

    print(f"Valor final de lista1: {lista1}")
    print(f"Valor final de lista2: {lista2}")

    print(
        "\nPara imitar la asignacion por valor y no por referencia se puede hacer lo siguiente:\n"
        "\tlista1 = [1, 2, 3]\n"
        "\tlista2 = list(lista1)\n"
        "\tlista2.append(4)\n"
        "Al usar un constructor se enfatiza en crear un nuevo espacio en memoria para lista2."
    )

    lista1 = [1, 2, 3]
    lista2 = list(lista1)
    lista2.append(4)

    print(f"Valor final de lista1: {lista1}")
    print(f"Valor final de lista2: {lista2}")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 06 - Valor y Referencia")
    print("-" * 20)

    val_ref_intro()

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
