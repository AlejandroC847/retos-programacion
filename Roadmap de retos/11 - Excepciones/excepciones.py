"""Módulo que muestra el uso de excepciones y como capturarlas, ademas de
como crear excepciones personalizadas y ejemplifica varias de las excepciones mas comunes.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/27"

import os

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

def excepciones():
    """Introducción a las excepciones. Se muestra una lista descriptiva de ellas"""
    print("Lista de excepciones:\n")

    print("\tDE LÓGICA Y ENTORNO:\n")
    print("> AttributeError: "
        "Se lanza cuando una referencia o asignación de atributo falla "
        "(ej: intentar acceder a self.no_existe)."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        x=10
        x.append(5)
    except AttributeError as e:
        print(f"La variable no tiene el atributo deseado: {e}")

    print("> ValueError: "
        "Se lanza cuando una función recibe un argumento con el "
        "tipo correcto pero un valor inapropiado."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        int("Hola")
    except ValueError as e:
        print(f"Valor inadecuado: {e}")

    print("> TypeError: "
        "Ocurre cuando una operación o función se aplica a un objeto de tipo inapropiado.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        "texto" + 5
    except TypeError as e:
        print(f"Tipo inválido: {e}")

    print("> NameError: "
        "Se lanza cuando no se encuentra un nombre local o global (variable no definida).")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        print(variable_inexistente) # type: ignore
    except NameError as e:
        print(f"No existe la variable: {e}")

    print("> IndexError: "
        "Ocurre cuando intentas acceder a un índice de una secuencia "
        "(lista, tupla) que está fuera de rango."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        lista = [1, 2]
        print(lista[4])
    except IndexError as e:
        print(f"Se intento acceder a un indice invalido: {e}")


    print("> KeyError: "
        "Se lanza cuando intentas acceder a una clave que no existe en un diccionario.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        diccionario = {"a": 1}
        print(diccionario["b"])
    except KeyError as e:
        print(f"Clave inaccesible: {e}")

    print("> ZeroDivisionError: "
        "Lanzada cuando el segundo argumento de una división o módulo es cero.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        5 / 0
    except ZeroDivisionError as e:
        print(f"Division sobre 0: {e}")


    print("\n\tDe entrada/salida y sistemas")
    print("> IOError / OSError: "
        "Error relacionado con operaciones del sistema operativo "
        "(fallo al abrir un archivo, falta de permisos)."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        os.open("/", os.O_RDWR)
    except OSError as e:
        print(f"Error del sistema: {e}")

    print("> FileNotFoundError: "
        "Un caso específico de OSError cuando no se encuentra un archivo.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        with open("archivo_que_no_existe.txt", "r", encoding="utf-8") as f:
            contenido = f.read()    #pylint: disable=unused-variable  # noqa: F841
    except FileNotFoundError as e:
        print(f"Archivo o directorio no encontrado: {e}")

    print("> PermissionError: "
        "Ocurre cuando el sistema operativo deniega el acceso "
        "(ej: intentaste ejecutar emplear sin tener permisos en tu clase)."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        def abrir_caja_fuerte(usuario):
            if usuario != "Gerente":
                raise PermissionError("Acceso denegado: solo el Gerente puede abrir la caja.")
            return "Caja abierta"

        abrir_caja_fuerte("Programador")
    except PermissionError as e:
        print(f"Error de permisos (personalizado): {e}")

    print("\n\tDe ejecución")
    print("> RuntimeError: "
        "Lanzada cuando ocurre un error que no cae bajo ninguna otra categoría.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        lista = [1, 2, 3]
        for i in lista:
            lista.remove(i) # Esto altera el tamaño de la lista durante la iteración
    except RuntimeError as e:
        print(f"Error inesperado en tiempo de ejecución: {e}")

    print("> NotImplementedError: "
        "Se usa para indicar que un método debe ser sobrescrito en la subclase "
        "(muy útil en jerarquías). Se lanza manualmente."
    )
    print("\tEjemplo de atrapar la excepción: ")
    try:
        class Animal:
            """Foo"""
            def hablar(self):
                """Foo"""
                raise NotImplementedError(
                    "Las subclases deben implementar el método 'hablar'"
                )
        class Perro(Animal): #pylint: disable=abstract-method
            """Foo"""
        p = Perro()
        p.hablar()
    except NotImplementedError as e:
        print(f"La subclase debe implementar tambien (Personalizado): {e}")

    print("> ImportError: "
        "Se lanza cuando una sentencia import tiene problemas.")
    print("\tEjemplo de atrapar la excepción: ")
    try:
        import modulo_inexistente
    except ImportError as e:
        print(f"No se pudo importar: {e}")

    print("> MemoryError: "
        "Ocurre cuando una operación se queda sin memoria.")
    print("\tEjemplo de atrapar la excepción: ")
    # Ejemplo: Intentar crear una estructura de datos absurdamente grande
    try:
        lista_gigante = [0] * (10**18) #pylint: disable=unused-variable  # noqa: F841
    except MemoryError:
        print("No hay suficiente memoria")

class MiErrorPersonalizado(Exception):
    """Excepción para mis errores personalizados."""
    def __init__(self, mensaje, error_code):
        super().__init__(mensaje)
        self.error_code = error_code

def funcion_prueba(arg1: str, arg2: int):
    """Función que lanza algunas excepciones para controlar errores"""
    if not isinstance(arg1, str):
        raise TypeError("Se esperaba una cadena como segundo argumento, "
                        f"se recibio {type(arg1).__name__}")

    if arg2 < 0:
        raise ValueError("El primer argumento debe ser un número positivo.")

    if arg1 != "Contraseña":
        raise MiErrorPersonalizado("No se introdujo la palabra clave", 1)

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 40)
    print("Roadmap 11 - Excepciones")
    print("-" * 40)

    excepciones()

    print("\nEjemplo Practico:")
    try:
        funcion_prueba("Macaco", 2)
        print("Función ejecutada correctamente")
    except (TypeError, ValueError, MiErrorPersonalizado) as e:
        print(f"Se lanzó una excepción de tipo {type(e).__name__}: {e}")
    finally:
        print("Termino la ejecución")

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
