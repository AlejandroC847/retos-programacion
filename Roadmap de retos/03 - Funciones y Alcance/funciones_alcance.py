"""Este módulo contiene una serie de ejemplos prácticos sobre la creación, 
invocación y comportamiento de las funciones en Python, cubriendo:
- Tipos de parámetros y retornos.
- Funciones anidadas y orden superior.
- Manejo de alcances (scopes) global y local.
- Aplicación de lógica de control mediante retos algorítmicos.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/16"

import os
CONST_GLOBAL = 3.14

#pylint: disable=unused-variable

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def no_param_no_ret():
    """Esta función no recibe parámetros y no retorna ningún valor"""
    print("\nEsta función no recibe ni retorna nada")

def some_param_no_ret(*args):
    """Esta función recibe un número variable de argumentos
    y los imprime en consola.
    """
    print("\nEsta función recibio los siguientes parametros:")
    print(*args, sep= " ")
    print("Pero no retorna nada.")

def param_ret(*args):
    """Esta función recibe un número variable de argumentos
    y retorna una tupla con dichos valores.
    """
    print("\nEsta función recibio parametros")
    print("Y ha retornado la tupla...")
    return args

def func_in_func():
    """Esta función demuestra el concepto de funciones anidadas y el alcance de las variables."""

    print("\nEsta función padre no recibe parametros")
    valor = 5
    print(f"Se llama a la función hija con el valor: {valor}.")
    def subfunc(val):
        print(f"Esta es la función hija y recibio el argumento {val}.")
        print(f"Se accede a la constante global con valor {CONST_GLOBAL}")
        # num = 3
    subfunc(valor)
    try:
        print(num)
    except NameError as err:
        print(f"No se tiene acceso a la variable local '{err.name}'")

def ejercicio(cad1: str, cad2: str) -> int:
    """Función que imprime números del 1 al 100, sustituyendo múltiplos de 3, 5 o ambos
    por cadenas de texto dadas, y retorna la cantidad de números impresos.
    """
    cant_num = 0
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += cad1
        if i % 5 == 0:
            output += cad2

        if output:
            print(f"{i}: {output}")
        else:
            print(i)
            cant_num += 1
    return cant_num

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 03 - Funciones y Alcance")
    print("-" * 20)

    no_param_no_ret()
    some_param_no_ret(5, 10, 15)

    print(param_ret(1, 2, 3, 4, 5))

    func_in_func()

    print(f"Cantidad de números sin texto: {ejercicio('Hola ', 'Mundo!')}")

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
