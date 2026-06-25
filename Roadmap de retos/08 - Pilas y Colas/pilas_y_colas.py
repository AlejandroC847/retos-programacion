"""Módulo que ejemplifica el funcionamiento de las estructuras LIFO (pilas) y las estructuras
FIFO (colas). Ofrece 3 funciones utilizables para cada estructura, y dos ejemplos practicos de uso.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/21"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

#region PILA

def add_element_stack(stack: list, *elements):
    """Agrega uno o más elementos al final de una pila, siguiendo el pensamiento LIFO

    Args:
        stack (list): Pila a la que se agregará el elemento.
        *elements: Elemento(s) de cualquier tipo para agregar a la pila. 

    Raises:
        TypeError: Si 'stack' no es una lista.
    """
    if not isinstance(stack, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!. "
            f"Se recibió {type(stack).__name__}"
        )

    for element in elements:
        stack.append(element)
        print(f"Pila: {element} insertado correctamente.")

def pop_element_stack(stack: list):
    """Extrae el último elemento agregado a la pila, siguiendo el pensamiento LIFO.

    Args:
        stack (list): Pila a la que se le extraerá un elemento.

    Raises:
        TypeError: Si 'stack' no es una lista.
        ValueError: Si la pila está vacía.
    """
    if not isinstance(stack, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!. "
            f"Se recibió {type(stack).__name__}"
        )
    if not stack:
        raise ValueError("No se pueden extraer elementos de una pila vacía!")

    return stack.pop()

def drain_stack(stack: list):
    """Extrae todos los elementos de la pila, siguiendo el pensamiento LIFO.

    Args:
        stack (list): Pila que se vaciará

    Raises:
        TypeError: Si 'stack' no es una lista.
        ValueError: Si la pila está vacía.
    """

    if not isinstance(stack, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!."
            f"Se recibió {type(stack).__name__}"
        )
    if not stack:
        raise ValueError("No se pueden extraer elementos de una pila vacía!")

    extracted = []

    while stack:
        extracted.append(stack.pop())

    return extracted

#endregion

#region COLA

def add_element_queue(queue: list, *elements):
    """Agrega uno o más elementos al principio de una cola, siguiendo el pensamiento FIFO

    Args:
        queue (list): Cola a la que se agregará el elemento.
        *elements: Elemento(s) de cualquier tipo para agregar a la cola. 

    Raises:
        TypeError: Si 'queue' no es una lista.
    """
    if not isinstance(queue, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!. "
            f"Se recibió {type(queue).__name__}"
        )

    for element in elements:
        queue.append(element)
        print(f"Cola: {element} insertado correctamente.")

def pop_element_queue(queue: list):
    """Extrae el primer elemento agregado a la cola, siguiendo el pensamiento FIFO.

    Args:
        queue (list): Cola a la que se le extraerá un elemento.

    Raises:
        TypeError: Si 'queue' no es una lista.
        ValueError: Si la cola está vacía.
    """
    if not isinstance(queue, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!. "
            f"Se recibió {type(queue).__name__}"
        )
    if not queue:
        raise ValueError("No se pueden extraer elementos de una cola vacía!")

    return queue.pop(0)

def drain_queue(queue: list):
    """Extrae todos los elementos de la cola, siguiendo el pensamiento FIFO.

    Args:
        queue (list): Cola que se vaciará.

    Raises:
        TypeError: Si 'queue' no es una lista.
        ValueError: Si la cola está vacía.
    """

    if not isinstance(queue, list):
        raise TypeError(
            "Se esperaba una lista como primer argumento!."
            f"Se recibió {type(queue).__name__}"
        )
    if not queue:
        raise ValueError("No se pueden extraer elementos de una cola vacía!")

    extracted = []

    while queue:
        extracted.append(queue.pop(0))

    return extracted

#endregion

#region Navegador web

def nav_web():
    """Simulador de navegador.

    Muestra el funciónamiento elemental de la navegacion entre sitios web y los historiales
    tanto pasado como futuro.
    Se navega entre dos listas que representan el historial de un navegador, agregando y
    extrayendo elementos de cada una respecto a la acción.
    """

    back_cmds = ("back", "atras")
    forward_cmds = ("forward", "adelante")
    exit_cmds = ("exit", "salir")

    history_back = []
    history_forward = []
    actual_page = "Main Page"

    exit_flag = False

    while not exit_flag:
        _clear_console()
        print("\tSimulador de Navegador")
        action = input(
            f"Estás en {actual_page}. ¿Qué deseas hacer?\n"
            "> 'Back' / 'Atras': Volver una página atrás"
            "> 'Forward' / 'Adelante': Ir una página adelante"
            "> Cualquier otra cosa sera el nombre de un sitio"
            "> 'Exit' / 'Salir': Cerrar navegador"
            "Acción: "
        )

        if action.lower() in exit_cmds:
            exit_flag = True
            continue
        elif action.lower() in back_cmds:
            if history_back:
                add_element_stack(history_forward, actual_page)
                actual_page = pop_element_stack(history_back)
            else:
                print("No hay paginas anteriores en el historial.")
            _enter_to_continue()
        elif action.lower() in forward_cmds:
            if history_forward:
                add_element_stack(history_back, actual_page)
                actual_page = pop_element_stack(history_forward)
            else:
                print("No hay paginas posteriores en el historial.")
            _enter_to_continue()
        else:
            add_element_stack(history_back, actual_page)
            actual_page = action
            history_forward.clear()
            _enter_to_continue()

    print("\nSaliendo del navegador...")
    _enter_to_continue()

#endregion

#region Impresora

def printer():
    """Simulador de impresora.

    Muestra el funcionamiento elemental de una cola de impresión. Se hace uso de una cola para
    gestionar los archivos que faltan por imprimir o los nuevos que se agregan.
    """

    print_cmds = ("print", "imprimir")
    exit_cmds = ("exit", "salir")
    exit_flag = False
    print_queue = []

    while not exit_flag:
        _clear_console()
        print("\tSimulador de Impresora")
        action = input(
            f"{"Cola de impresión pendiente. " if print_queue else ""}¿Qué deseas hacer?\n"
            "> 'Imprimir' / 'Print': Continuar imprimiendo"
            "> Cualquier otra cosa se agrega a la cola de impresión"
            "> 'Exit' / 'Salir': Apagar impresora"
            "Acción: "
        )

        if action.lower() in exit_cmds:
            exit_flag = True
            continue
        elif action.lower() in print_cmds:
            if print_queue:
                print(f"Imprimiendo...\n{pop_element_queue(print_queue)}")
            else:
                print("La cola de impresión está vacía")
            _enter_to_continue()
        else:
            add_element_queue(print_queue, action)
            print("Agregado a la cola de impresión correctamente")
            _enter_to_continue()

    print("\nApagando Impresora...")
    _enter_to_continue()

#endregion

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 08 - Pilas y Colas")
    print("-" * 20)

        # Estructura Basica

    print("Estructura básica:")

    print("\n\tPila")
    pila = [1, 2, 3]
    print(f"Pila actual: {pila}")

    add_element_stack(pila, 4, 5, 6)
    print(f"Se extrajo de la pila el elemento: {pop_element_stack(pila)}")
    print(f"Pila actual: {pila}")
    print(f"Se extrajeron todos los elementos de la pila: {drain_stack(pila)}")

    print("\n\tCola")
    cola = [1, 2, 3]
    print(f"Cola actual: {cola}")

    add_element_queue(cola, 4, 5, 6)
    print(f"Se extrajo de la cola el elemento: {pop_element_queue(cola)}")
    print(f"Cola actual: {cola}")
    print(f"Se extrajeron todos los elementos de la cola: {drain_queue(cola)}")

        # Navegador

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
