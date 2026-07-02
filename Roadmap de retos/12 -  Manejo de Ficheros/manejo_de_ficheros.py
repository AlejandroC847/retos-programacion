"""Gestor de Inventario para Ventas.

Este módulo proporciona la clase SalesManager para gestionar el inventario 
de una empresa, incluyendo operaciones de persistencia de datos en archivos JSON, 
validación de tipos y visualización formateada de productos.

El módulo utiliza `pathlib` para el manejo de rutas y `json` para la persistencia.

Contenido:
    - SalesManager: Clase principal para la gestión de productos.
    - Funciones de utilidad: _clear_console, _enter_to_continue.
    - Función de ejemplo practico de manejo de archivos: file_management.
"""

__author__ = "Alejandro Cortés"
__date__ = "2026/06/29"

import os
import json
from pathlib import Path

GITHUB_USER = "AlejandroC847"
FILE_NAME = "inventario.json"
FILE_PATH = Path(__file__).parent / FILE_NAME

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("\n\nPresione enter para continuar...")

def files_management():
    """Ejemplifica el manejo de archivos.
    Muestra un ejemplo de escritura y eliminacion de un archivo"""
    file_name = GITHUB_USER + ".txt"
    my_name = "Alejandro Cortés"
    age = "20"
    prefer_programming_language = "Python"

    with open(
        file=file_name,
        mode="w",            # Lectura y Escritura (el archivo debe existir)
        buffering=-1,         # Buffer por defecto del sistema
        encoding="utf-8",     # Soporte para tildes y caracteres especiales
        errors="strict",      # Lanza error si hay caracteres que no puede decodificar
        newline="\n"          # Manejo estándar de saltos de línea
    ) as f:
        f.write("Información\n")

        print(
                f"Usuario de GitHub: {GITHUB_USER}\n"
                f"Nombre: {my_name}\n"
                f"Edad: {age}\n"
                f"Lenguaje Preferido: {prefer_programming_language}"
        , file=f)

            # Obtener Informacion
        print(f"¿Está el archivo cerrado? {f.closed}")
        print(f"Nombre del archivo: {f.name}")
        print(f"Codificación utilizada: {f.encoding}")

    print("Ahora puede revisar el archivo en su explorador, posteriormente sera eliminado...")
    _enter_to_continue()

    if os.path.exists(file_name):
        os.remove(file_name)
        print("Archivo eliminado con éxito.")

class SalesManager():
    """Administrador del inventario de la empresa"""
    def __init__(self):
        self.file = FILE_PATH
        self.products = {}
        self.load_changes()

    def _product_exist(self, product: str):
        if not isinstance(product, str):
            raise TypeError("Se esperaba un nombre de producto en formato de texto"
                            f"Se recibió: {type(product).__name__}"
                        )
        return product.lower() in [p.lower() for p in self.products]

    def add_products(self, **kwargs: dict[str, float | int]):
        """Agrega uno o varios productos al inventario.

        Args:
            **kwargs: Pares nombre_producto (str) y un diccionario con los datos 
                del producto, ej: {'price': 15000, 'units_sold': 8}.

        Returns:
            None: Modifica directamente el estado de self.products.

        Raises:
            TypeError: Si los datos de entrada no tienen el formato esperado.
            ValueError: Si los valores numéricos son negativos.
        """

        if kwargs:
            for product_name, data in kwargs.items():
                if not isinstance(product_name, str): #?Por defecto se pasa como str, pero igual es defensivo
                    raise TypeError(
                        "Se esperaba un nombre de producto de tipo cadena. "
                        f"Se recibió: {type(product_name).__name__}.\n"
                    )
                if not isinstance(data, dict) or "price" not in data or "units_sold" not in data:
                    raise TypeError(
                        f"El producto '{product_name}' debe ser un dict con 'price' y 'units_sold'. "
                        f"Se recibió: {type(data).__name__}"
                    )

                product_price = data["price"]
                units_sold = data["units_sold"]


                if not isinstance(product_price, (int, float)) or product_price < 0:
                    raise ValueError(
                        f"Precio inválido para {product_name}. "
                        f"Debe ser un número >= 0. Se recibió '{product_price}'."
                    )

                if not isinstance(units_sold, int) or units_sold < 0:
                    raise ValueError(
                        f"Cantidad inválida para {product_name}. "
                        f"Debe ser un número >= 0. Se recibió {units_sold}."
                    )

                if self._product_exist(product_name):
                    print(
                        f"El producto '{product_name}' ya existe. "
                        "Si desea actualizar el precio recurra a la función adecuada para ello."
                    )
                    _enter_to_continue()
                    continue

                self.products[product_name] = {
                    "price": float(product_price),
                    "units_sold": units_sold
                }
        else:
            while True:
                _clear_console()
                print("\tInsertar nuevo producto:")

                # Nombre del producto
                product_name = input("Ingresa nombre de producto: ")
                if self._product_exist(product_name):
                    print(
                        f"El producto '{product_name}' ya existe. "
                        "Si desea actualizar el precio recurra a la función adecuada para ello."
                    )
                    _enter_to_continue()
                    continue
                # Precio
                try:
                    product_price = float(input("Ingresa el precio: "))
                    if product_price < 0:
                        raise ValueError
                except ValueError:
                    print(
                        "Ingresa un número válido para el precio!. "
                        "Debe ser un número mayor o igual a 0."
                    )
                    _enter_to_continue()
                    continue
                # Precio
                try:
                    units_sold = int(input("Ingresa la cantidad vendida: "))
                    if units_sold < 0:
                        raise ValueError
                except ValueError:
                    print(
                        "Ingresa un número válido para la cantidad de unidades vendidas! "
                        "Debe ser un número mayor o igual a 0."
                    )
                    _enter_to_continue()
                    continue

                self.products[product_name] = {"price": product_price, "units_sold": units_sold}

                exit_flag = input("Desea seguir agregando productos? S/N: ")
                if exit_flag.lower() in ["n", "no"]:
                    break
        self.save_changes(True)

    def check_inventory(self):
        """Genera y muestra una tabla formateada con el inventario actual.

        Calcula dinámicamente el ancho necesario para cada columna basándose en 
        la longitud del texto más largo (encabezados o datos), asegurando una 
        presentación alineada. Si el inventario está vacío, muestra un mensaje.

        Returns:
            None: La función imprime la tabla directamente en la salida estándar.
        """
        if not self.products:
            print("\tInventario\n")
            print("No hay productos registrados!")
            return

        header = ["Producto", "Precio", "Vendidos"]
        col_widths = [
            max(len(header[0]), max((len(p) for p in self.products), default=0)),
            max(len(header[1]),
                    max((len(f"{v['price']}") for v in self.products.values()), default=0)),
            max(len(header[2]),
                max((len(f"{v['units_sold']}") for v in self.products.values()), default=0))
        ]

        def create_border(char_left, char_mid, char_right, sep):
            parts = [(sep * (w + 2)) for w in col_widths]
            return char_left + char_mid.join(parts) + char_right

        center_title = (' ' * (sum(col_widths) // 2))
        print(f"{center_title}Inventario\n")

        # Borde inicial y encabezados
        print(create_border("┌", "┬", "┐", "─"))
        print(f"│ {header[0].ljust(col_widths[0])} "
            f"│ {header[1].ljust(col_widths[1])} "
            f"│ {header[2].ljust(col_widths[2])} │"
        )
        # Contenido
        for product, values in self.products.items():
            print(create_border("├", "┼", "┤", "─"))
            print(f"│ {product.ljust(col_widths[0])} "
                f"│ {str(values['price']).ljust(col_widths[1])} "
                f"│ {str(values['units_sold']).ljust(col_widths[2])} │"
            )
        # Borde final
        print(create_border("└", "┴", "┘", "─"))

        _enter_to_continue()

    def update_product(self, product_name:str, price: float | int, units_sold: int):
        """Actualiza la información de un producto existente en el inventario.

        Busca el producto por su nombre y, si existe, modifica su precio 
        y la cantidad de unidades vendidas con los nuevos valores proporcionados.

        Args:
            product_name (str): El nombre del producto a actualizar.
            price (float | int): El nuevo precio del producto (debe ser >= 0).
            units_sold (int): La nueva cantidad de unidades vendidas (debe ser >= 0).

        Returns:
            None: Modifica el estado interno de self.products.

        Raises:
            TypeError: Si el tipo de dato del nombre del producto es incorrecto.
            ValueError: Si el precio o las unidades vendidas no cumplen con ser >= 0.
        """
        if not isinstance(product_name, str):
            raise TypeError("Se esperaba un nombre de producto en formato de texto. "
                            f"Se recibió {type(product_name).__name__}")

        if not self._product_exist(product_name):
            print("Ese producto no existe!")
            _enter_to_continue()
            return

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError(
                f"Precio inválido para {product_name}. "
                f"Debe ser un número >= 0. Se recibió '{price}'."
            )

        if not isinstance(units_sold, int) or units_sold < 0:
            raise ValueError(
                f"Cantidad inválida para {product_name}. "
                f"Debe ser un número >= 0. Se recibió {units_sold}."
            )

        self.products[product_name]["price"] = float(price)
        self.products[product_name]["units_sold"] = units_sold

        print(f"Se actualizó el producto '{product_name}'\n"
            f"\tPrecio: {price}\n"
            f"\tVendidos: {units_sold}\n"
        )

        _enter_to_continue()
        self.save_changes(True)

    def delete_product(self, product: str):
        """Solicita confirmación y elimina un producto del inventario.

        Verifica si el producto existe antes de pedir confirmación al usuario.
        Si el usuario confirma, elimina la entrada del diccionario self.products.

        Args:
            product (str): Nombre del producto a eliminar.

        Raises:
            TypeError: Si el nombre proporcionado no es un string.
        """

        if not isinstance(product, str):
            raise TypeError("Se esperaba un nombre de producto en formato de texto. "
                            f"Se recibió {type(product).__name__}")

        if not self._product_exist(product):
            print("Ese producto no existe!")
            _enter_to_continue()
            return

        confirm = input("Seguro que quieres eliminar este producto? S/N: ")
        if  confirm.lower() in ["s", "si", "y", "yes"]:
            self.products.pop(product)
            print(f"El producto '{product}' fue eliminado correctamente.")
        else:
            print(f"El producto '{product}' no pudo ser eliminado.")

        _enter_to_continue()

        self.save_changes(True)

    def clean_inventory(self):
        """Elimina permanentemente todo el inventario de memoria y del archivo local.

        Solicita confirmación explícita al usuario. Si es afirmativa, vacía el 
        diccionario self.products y elimina el archivo JSON del sistema.

        Returns:
            None: Modifica self.products y el sistema de archivos.
        """
        confirm = input("Estas seguro de eliminar el inventario?\n"
                        "Esta acción no se puede deshacer! S/N: "
                    )

        if confirm.lower() in ["s", "si", "y", "yes"]:
            print("\tEliminando registros de inventario...")
            self.products = {}

            if os.path.exists(self.file):
                os.remove(self.file)
                print("Archivo eliminado con éxito.")
            else:
                print("El fichero no fue encontrado.!")
        else:
            print("Se anulo la eliminación del inventario.")

        _enter_to_continue()

    def load_changes(self):
        """Carga los datos desde el archivo JSON de forma segura."""
        if not os.path.exists(self.file):
            print("No pudieron recuperase datos locales")
            _enter_to_continue()
            return
        try:
            with open(self.file, "r", encoding="utf-8")as f:
                self.products = json.load(f)
            print("Datos recuperados desde el archivo.")
        except(json.JSONDecodeError, OSError) as e:
            print(f"Error al cargar datos del archivo: {e}")
            self.products = {}
        finally:
            _enter_to_continue()

    def save_changes(self, silent: bool = False):
        """Guarda los cambios actuales en el archivo JSON."""

        if not self.products:
            print("No hay registros para guardar.")
            if os.path.exists(self.file):
                print("Existe un archivo sin registros. Eliminando...")
                os.remove(self.file)
            _enter_to_continue()
            return

        try:
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(self.products, f, indent=4)
            if not silent:
                print("Se guardaron los datos correctamente")
        except OSError as e:
            print(f"Error al guardar datos en el archivo: {e}")
        finally:
            _enter_to_continue()

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 40)
    print("Roadmap 12 - Manejo de Ficheros")
    print("-" * 40)

    #files_management()
    administrador = SalesManager()

    administrador.add_products(
        tv={"price": 15000.0, "units_sold": 8},
        colchon={"price": 6000.0, "units_sold": 7},
        bici={"price": 2800, "units_sold": 15},
        laptop={"price": 15000, "units_sold":  3}
    )

    administrador.check_inventory()

    administrador.update_product("tv", 8000, 12)
    administrador.delete_product("bici")

    administrador.check_inventory()

    administrador.clean_inventory()

    administrador.save_changes()

    _enter_to_continue()

# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
