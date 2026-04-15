"""
Moódulo para realizar las pruebas del módulo area_poligono.py.
Se utiliza assert para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/14"

import area_poligono as area
from pytest import approx, raises
from colorama import Fore, Style, init

init(autoreset=True)

def test_areas():
    """
    Ejecuta las pruebas esperadas por posibles casos aplicados al metodo calcular_area()
    en las varias clases de polígonos
    """
    assert area.Triangulo(10,5).calcular_area() == approx(25)
    assert area.Cuadrado(2.5).calcular_area() == approx(6.25)
    assert area.Rectangulo(12,8).calcular_area() == approx(96)
    assert area.Trapecio(8.2,4.4,3).calcular_area() == approx(18.9)
    assert area.Rombo(5,3).calcular_area() == approx(7.5)
    assert area.PoligonoRegular(24,3.46).calcular_area() == approx(41.52)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅Calculos de áreas esperados...")

def test_errores():
    """Verifica que la función maneje correctamente entradas de tipos inválidos."""

    casos_invalidos = [
        "Diez",         # String
        "21",           # String numérico
        [4],            # Lista
        None            # NoneType
    ]

    for caso in casos_invalidos:
        with raises(TypeError):
            area.Cuadrado(caso)

    casos_invalidos = [0,-5,-1.2] # Negativos

    for caso in casos_invalidos:
        with raises(ValueError):
            area.Triangulo(caso, 16)

#=========================
#Ejecución Principal
#=========================
if __name__ == "__main__":
    try:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_areas()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except AssertionError:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
