"""Método para introducir el concepto de las clases en python.
Se hace uso de dos clases personalizadas para las estructuras de pila y cola,
donde cada clase tiene los métodos de las operaciones de cada estructura
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/24"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

class Example():
    """Clase de prueba.

    Recibe dos argumentos al instanciarse, los asigna como atributos y permite imprimirlos.
    """

    def __init__(self, arg_test1, arg_test2):
        self.test_attribute_1 = arg_test1
        self.test_attribute_2 = arg_test2

    def print_args(self):
        "Imprime los atributos del objeto"
        print(f"Primer Atributo: {self.test_attribute_1}")
        print(f"Segundo Atributo: {self.test_attribute_2}")

def implement_example():
    """Instancia la clase de ejemplo pasandole dos argumentos, se asignan como atributos
    y se imprimen.
    """
    object_example = Example("Prueba", "Testeo")
    object_example.print_args()

#region PILA

class Stack():
    """Clase simuladora de pila que permite acceder a los elementos y realizar operaciones LIFO."""
    def __init__(self, *values):
        self.stack = list(values)

    def __str__(self):
        return f"Stack({self.stack})"

    def add_element(self, *elements):
        """Agrega elementos a la pila interna"""
        self.stack.extend(elements)

    def pop_element(self):
        """Extrae el último elemento (LIFO) agregado a la pila"""
        if not self.stack:
            raise ValueError("No se pueden extraer elementos de una pila vacía!")
        return self.stack.pop()

    def drain(self):
        """Extrae todos los elementos de la pila siguiendo la estructura LIFO"""
        if not self.stack:
            raise ValueError("No se pueden extraer elementos de una pila vacía!")

        extracted = []
        while self.stack:
            extracted.append(self.stack.pop())

        return extracted

    @property
    def size(self):
        """Exporta la cantidad de elementos en la pila"""
        return len(self.stack)

#endregion

#region COLA

class Queue():
    """Clase simuladora de cola que permite acceder a los elementos y realizar operaciones FIFO"""

    def __init__(self, *values):
        self.queue = list(values)

    def __str__(self):
        return f"Queue({self.queue})"

    def add_element(self, *elements):
        """Agrega elementos a la cola interna."""
        self.queue.extend(elements)

    def pop_element(self):
        """Extrae el primer elemento (FIFO) agregado a la cola."""
        if not self.queue:
            raise ValueError("No se pueden extraer elementos de una cola vacía!")
        return self.queue.pop(0)

    def drain(self):
        """Extrae todos los elementos de la cola siguiendo la estructura FIFO."""
        if not self.queue:
            raise ValueError("No se pueden extraer elementos de una cola vacía!")

        extracted = []
        while self.queue:
            extracted.append(self.queue.pop(0))

        return extracted

    @property
    def size(self):
        """Exporta la cantidad de elementos de la cola."""
        return len(self.queue)

#endregion

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 08 - Pilas y Colas")
    print("-" * 20)

    implement_example()

    print("Ejemplo de clase Stack:\n")
    mi_pila = Stack(1, 2, 3)
    print(f"Iniciada la pila como: {mi_pila}")
    mi_pila.add_element(4, 5)
    mi_pila.pop_element()
    print(f"Ahora quedan {mi_pila.size} elementos en la pila.")
    mi_pila.drain()
    print(f"Por ultimo...{mi_pila}.")

    print("Ejemplo de clase Queue:\n")
    mi_cola = Queue(1, 2, 3)
    print(f"Iniciada la cola como: {mi_cola}")
    mi_cola.add_element(4, 5)
    mi_cola.pop_element()
    print(f"Ahora quedan {mi_cola.size} elementos en la cola.")
    mi_cola.drain()
    print(f"Por ultimo...{mi_cola}.")

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
