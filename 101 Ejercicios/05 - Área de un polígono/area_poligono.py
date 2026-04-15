"""
Módulo que permite calcular el área de un poligono por medio de los datos necesarios para ello.
Por medio de clases que heredan de una clase principal se pueden calcular los poligonos que se
muestran a continuación junto con los datos requeridos en cada caso.
- Triangulo: base, altura
- Cuadrado: lado
- Rectangulo: base, altura
- Trapecio: base mayor, base menor, altura
- Rombo: diagonal mayor, diagonal menor
- Cualquier poligono regular: perimetro, apotema
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/11"

from abc import ABC, abstractmethod

class Poligono(ABC):
    """Clase abstracta que define la estructura base para cualquier polígono."""

    def __init__(self, *dimensiones):
        for dim in dimensiones:
            if not isinstance(dim, (int, float)):
                raise TypeError(f"El valor '{dim}' debe ser numerico.")
            if dim <= 0:
                raise ValueError(f"El valor '{dim}' debe ser un entero positivo.")

    @abstractmethod
    def calcular_area(self):
        """Calcula el área del polígono. La implementación se encuentra en las subclases."""

class Triangulo(Poligono):
    """Clase para representar un Triangulo.

    Args:
        base (float): Longitud de la base del triangulo.
        altura (float): Altura del triangulo.
    """

    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del triangulo basandos en sus medidas actuales.

        Returns:
            float: Área total del triángulo.
        """
        resultado = (self.base * self.altura) / 2
        return resultado

    def __str__(self):
        return f"Triángulo [Base: {self.base}, Altura: {self.altura}]"

class Cuadrado(Poligono):
    """Clase para representar un cuadrado

    Args:
        lado (float): Longitud de cada lado del cuadrado.
    """

    def __init__(self, lado):
        super().__init__(lado)
        self.lado = lado

    def calcular_area(self):
        """Calcula el área del cuadrado basandose en sus medidas actuales.

        Returns:
            float: Área total del cuadrado.
        """
        resultado = self.lado ** 2
        return resultado

    def __str__(self):
        return f"Cuadrado [Lado: {self.lado}]"

class Rectangulo(Poligono):
    """Clase para representar un Rectangulo.

    Args:
        base (float): Longitud de la base del rectangulo.
        altura (float): Altura del rectangulo.
    """


    def __init__(self, base, altura):
        super().__init__(base, altura)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectangulo basandose en sus medidas actuales.

        Returns:
            float. Área total del rectangulo.
        """
        resultado = self.base * self.altura
        return resultado

    def __str__(self):
        return f"Rectangulo [Base: {self.base}, Altura: {self.altura}]"

class Trapecio(Poligono):
    """Clase para representar un Trapecio.

    Args:
        base_mayor (float): Longitud de la base mayor del trapecio.
        base_menor (float): Longitud de la base menor del trapecio.
        altura (float): Altura del trapecio.
    """

    def __init__(self, base_mayor, base_menor, altura):
        super().__init__(base_mayor, base_menor, altura)
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del trapecio basandose en sus medidas actuales.

        Returns:
            float: Área total del trapecio.
        """

        resultado = (self.base_mayor + self.base_menor) * self.altura / 2
        return resultado

    def __str__(self):
        return (
            f"Trapecio [Base Mayor: {self.base_mayor}, "
            f"Base Menor: {self.base_menor}, Altura: {self.altura}]"
        )

class Rombo(Poligono):
    """Clase para representar un Rombo

    Args:
        diagonal_mayor (float): Longitud de la diagonal mayor.
        diagonal_menor (float): Longitud de la diagonal menor.
    """

    def __init__(self, diagonal_mayor, diagonal_menor):
        super().__init__(diagonal_mayor, diagonal_menor)
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        """Calcula el área del rombo basandose en sus medidas actuales.

        Returns:
            float: Área total del rombo.
        """
        resultado = self.diagonal_mayor * self.diagonal_menor / 2
        return resultado

    def __str__(self):
        return (
            f"Rombo [Diagonal Mayor: {self.diagonal_mayor}, Diagonal Menor: {self.diagonal_menor}]"
        )

class PoligonoRegular(Poligono):
    """Clase que representa un polígono regular

    Args:
        perimetro (float): Longitud del contorno del polígono.
        apotema (float): Distancia desde el centro del polígono hasta
        la mitad de alguno de sus lados.
    """

    def __init__(self, perimetro, apotema):
        super().__init__(perimetro, apotema)
        self.perimetro = perimetro
        self.apotema = apotema

    def calcular_area(self):
        """Calcula el área del polígono regular basandose en sus medidas actuales.

        Returns:
            float: Área total del polígono regular.
        """
        resultado = (self.perimetro * self.apotema) / 2
        return resultado

    def __str__(self):
        return f"Polígono regular [Perímetro: {self.perimetro}, Apotema: {self.apotema}]"

def imprimir_area(poligono: Poligono):
    """_

    Args:
        poligono (Poligono): Instancia de un poligono con sus medidas como parametros.

    Returns:
        float: Área calculada del polígono.
    """

    area = poligono.calcular_area()
    print(f"El área del {poligono} es de {area}")
    return area

# =========================
# Ejecución principal
# =========================
if __name__ == "__main__":
    imprimir_area(Triangulo(3,4))
    imprimir_area(Cuadrado(7))
    imprimir_area(Rectangulo(2,8))
    imprimir_area(Trapecio(5, 3,4))
    imprimir_area(Rombo(8,7))
    imprimir_area(PoligonoRegular(9,6))
