"""
Moódulo para realizar las pruebas del módulo aspect_ratio.py.
Se utiliza assert y pytest para verificar que se obtienen los resultados esperados.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/14"

import io
import aspect_ratio as ar
from pytest import raises
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

def test_ratio():
    """
    Ejecuta las pruebas esperadas por posibles casos aplicados a la funció procesar_imagen()
    """

    # Crear imagen ficticia en memoria
    img = Image.new('RGB', (1920, 1080))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_bytes = img_byte_arr.getvalue()
    _, w, h, rw, rh = ar.procesar_imagen(img_bytes) # Versión lógica
    assert (w, h, rw, rh) == (1920, 1080, 16, 9)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Cálculo de ratio esperado...")

def test_consultar_url():
    """Prueba la descarga de la imagen a partir de la URL."""
    url = "https://i.pinimg.com/736x/2d/0c/5d/2d0c5df19c058ba1b8eb7990af24a30c.jpg"
    resultado = ar.obtener_imagen(url)

    assert resultado is not None
    assert isinstance(resultado, bytes)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Manejo de url adecuado...")

def test_errores():
    """
    Verifica que el sistema maneje correctamente las entradas inválidas
    y tipos de datos incorrectos.
    """

    casos_invalidos_url = [123, ["http://link.com"], None]

    for caso in casos_invalidos_url:
        assert ar.obtener_imagen(caso) is None

    casos_invalidos_bytes = ["cadena de texto", 456, True]

    for caso in casos_invalidos_bytes:
        with raises((TypeError, AttributeError, Exception)):
            ar.procesar_imagen(caso)

    resultado = ar.procesar_imagen(None)
    assert resultado == (None, 0, 0, 0, 0)

    print(f"{Fore.GREEN}{Style.BRIGHT}✅ Pruebas de errores completadas con éxito.")

#=========================
#Ejecución Principal
#=========================
if __name__ == "__main__":
    try:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Ejecutando suite de pruebas...")

        test_ratio()
        test_consultar_url()
        test_errores()

        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ Todos los tests pasaron correctamente")
    except AssertionError:
        print(f"\n{Fore.RED}{Style.BRIGHT}❌ Los tests fallaron")
