"""Módulo que ejemplifica los conceptos de herencia y polimorfismo de clases.
Se integra una clase padre 'Animal' y las clases hijos 'Gato', 'Perro' y 'Conejo', cada una
con un método compartido pero con un comportamiento diferente.
Se integra tambien una clase padre 'Empleado', junto a sus clases hijas 'Gerente', 'LiderProyecto'
y 'Programador', todas heredan los métodos de 'Empleado' pero tambien tienen métodos independientes.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/25"

import os
import re

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

class Animal():
    """Super clase Animal. Define el nombre de la especie"""
    def __init__(self, regular_name: str = "ND"):
        self.regular_name = regular_name

class Gato(Animal):
    """Clase heredada de Animal. Asigna el nombre de Gato y define su sonido"""
    def __init__(self):
        super().__init__(regular_name = "Gato")

    def sonido(self):
        """Muestra en pantalla el sonido que hace el animal"""
        print(f"El {self.regular_name} maulla: 'Miau'.")

class Perro(Animal):
    """Clase heredada de Animal. Asigna el nombre de Perro y define su sonido"""
    def __init__(self):
        super().__init__(regular_name = "Perro")

    def sonido(self):
        """Muestra en pantalla el sonido que hace el animal"""
        print(f"El {self.regular_name} ladra: 'Guau'")

class Conejo(Animal):
    """Clase heredada de Animal. Asigna el nombre de Conejo y define su sonido"""
    def __init__(self):
        super().__init__(regular_name = "Conejo")

    def sonido(self):
        """Muestra en pantalla el sonido que hace el animal"""
        print(f"El {self.regular_name} chilla: 'AAAAAAAAAAAAAA *en agudo*'")

# Empleados
class Empleado():
    """Clase generica de empleados, contiene los atributos base para un empleado"""
    def __init__(self, name: str, employee_id: str):
        self.name = name
        self.id = employee_id
        self.empleados_a_cargo = []

    def __str__(self):
        information = (
            f"\nNombre: {self.name}\n"
            f"Cargo: {re.sub(r'([a-z])([A-Z])', r'\1 \2', type(self).__name__)}\n"
            f"ID: {self.id}\n"
        )

        if self.empleados_a_cargo:
            sub = '\n'.join([f'\t{e.name}' for e in self.empleados_a_cargo])
            information += f"Empleados a su cargo:\n{sub}\n"
        else:
            information +="No tiene empleados a su cargo\n"

        return information

    def _puede_emplear(self):
        """Si el Empleado puede tener a otros bajo su cargo. Por defecto retorna False"""
        return False

    def emplear(self, empleado: 'Empleado'):
        """Agregar empleado a su cargo"""

        if not self._puede_emplear():
            raise PermissionError(
                f"{self.__class__.__name__} no tiene permisos para gestionar personal."
            )

        if not isinstance(empleado, Empleado):
            raise ValueError(f"Se esperaba un empleado. Se recibió: {type(empleado).__name__}")

        self.empleados_a_cargo.append(empleado)

    def despedir(self, empleado: 'Empleado'):
        """Quitar de su cargo a algun empleado"""
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)

class Gerente(Empleado):
    """Plantilla de gerente principal"""

    def tomar_decision_estrategica(self, decision: str):
        """Simula el tomar desiciones importantes para la empresa"""
        print(f"La/el Gerente {self.name} ha tomado una decisión estratégica: {decision}.")

    def _puede_emplear(self):
        return True

class LiderProyecto(Empleado):
    """Plantilla de Lider de proyecto"""

    def planificar_proyecto(self, project_name):
        """Simula la gestion que ofrece el lider en un proyecto"""
        print(
            f"El Lider de Proyecto {self.name} está actualizando el tablero de tareas y"
            f" los plazos para el proyecto {project_name}."
        )
        return project_name

    def _puede_emplear(self):
        return True

class Programador(Empleado):
    """Programador general que trabaja en proyectos"""

    def escribir_codigo(self, proyecto):
        """Simula el proceso de produccion de software"""
        print(f"El programador {self.name} está escribiendo código para {proyecto}...")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 40)
    print("Roadmap 10 - Herencia y Polimorfismo")
    print("-" * 40)

    # Ejemplos Herencia y Polimorfismo

    print("Animales")

    animales = [Gato(), Perro(), Conejo()]

    for animal in animales:
        animal.sonido()

    # Empleados
    print("\nEmpresa")
    gerente = Gerente("Dani", 1)
    lider_proyectos_a = LiderProyecto("Manuela", 2)
    programador_1a = Programador("Alejandro", 3)
    programador_2a = Programador("Laura", 4)
    lider_proyectos_b = LiderProyecto("Manuel", 5)
    programador_1b = Programador("Sofia", 6)
    programador_2b = Programador("Carlos", 7)

    gerente.emplear(lider_proyectos_a)
    gerente.emplear(lider_proyectos_b)

    lider_proyectos_a.emplear(programador_1a)
    lider_proyectos_a.emplear(programador_2a)

    lider_proyectos_b.emplear(programador_1b)
    lider_proyectos_b.emplear(programador_2b)

    print(gerente)
    gerente.tomar_decision_estrategica("Contratar mas empleados ademas de el")

    print(lider_proyectos_a)
    proyecto_a =lider_proyectos_a.planificar_proyecto("Videojuego")
    print(programador_1a)
    programador_1a.escribir_codigo(proyecto_a)
    print(programador_2a)
    programador_2a.escribir_codigo(proyecto_a)

    print(lider_proyectos_b)
    proyecto_b =lider_proyectos_b.planificar_proyecto("Sistema CAA")
    print(programador_1b)
    programador_1b.escribir_codigo(proyecto_b)
    print(programador_2a)
    programador_2b.escribir_codigo(proyecto_b)

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
