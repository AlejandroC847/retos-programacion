"""
Manejar imagenes a partir de una url, mostrarlas en una ventana
emergente y calcular su aspect ratio.
Ratio = w / mcd(w,h) : h / mcd(w,h)
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/15"

import io
import tkinter as tk

import requests as r
from PIL import ImageTk, Image

MAX_WIDTH = 800
MAX_HEIGHT = 600

def obtener_imagen(url: str) -> bytes | None:
    """Obtiene el contenido de la url (que debe ser una imagen) y retorna el contenido en bytes.

    Args:
        url (str): Dirección http de la imagen en formato de texto,

    Returns:
        bytes: Contenido de la imagen extraída en bytes.
    """

    try:
        image = r.get(url, timeout=10)
        image.raise_for_status()

        content_type = image.headers.get('Content-Type', '')
        if 'image' not in content_type:
            print("Advertencia: El enlace no parece apuntar a una imagen.")
            return None

        # Retornamos el contenido en bytes (.content)
        return image.content

    except r.exceptions.RequestException as e:
        print(f"Error al conectar con la URL: {e}")
        return None

def procesar_imagen(imagen_en_bytes: bytes | None) -> Image.Image | None:
    """
    Convierte el contenido en bytes de la imagen en una imagen real en memoria.
    Obtiene las dimensiones de la imagen y su ratio de aspecto.

    Args:
        imagen_en_bytes (bytes  |  None): Recibe el contenido en bytes de la imagen (si fue
        extraída correctamente) o None (si no fue extraída correctamente)-.

    Returns:
        Image.Image | None: Retorna el objeto de la imagen si pudo procesarla o None si no pudo.
    """

    if imagen_en_bytes is None:
        print("Error: No se recibió una imagen en bytes")
        return None, 0, 0, 0, 0

    imagen_en_memoria = io.BytesIO(imagen_en_bytes)
    imagen_pil = Image.open(imagen_en_memoria)

    print(f"Tamaño de la imagen: {imagen_pil.size}")

    width, height = imagen_pil.size

    a = width
    b = height

    while b:
        a, b = b, a % b
    mcd = a
    # Alternativa: math.gcd(width, height)

    ratio_w = width // mcd
    ratio_h = height // mcd

    print(f"Ratio de la imagen: {ratio_w}:{ratio_h}")

    # Redimensionar imagen

    if width > MAX_WIDTH or height > MAX_HEIGHT:
        scaling_factor = min(MAX_WIDTH / width, MAX_HEIGHT / height)

        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        imagen_pil = imagen_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)

    return imagen_pil, width, height, ratio_w, ratio_h

def mostrar_imagen(imagen: Image.Image, w: int, h: int, ratio_w: int, ratio_h: int):
    """Inicializa una ventana de Tkinter y muestra la imagen recibida en ella.

    Args:
        imagen (Image.Image): Imagen lista para ser procesada por Tkinter.
    """

    if imagen is None:
        print("No hay imagen disponible para mostrar")
        return

    app = tk.Tk()
    app.title("Visor de Imagen")

    imagen_tk = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(app, image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    etiqueta_imagen.pack(padx=20, pady=20)

    etiqueta_medidas = tk.Label(app, text=f"Tamaño original: {w}x{h}")
    etiqueta_medidas.pack()

    etiqueta_ratio = tk.Label(app, text=f"Ratio: {ratio_w}:{ratio_h}")
    etiqueta_ratio.pack()

    app.mainloop()

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    DIRECCION = "https://i.pinimg.com/736x/22/21/12/222112c36704f8e08011c7c2da22c8f9.jpg"

    img, wi, hi, rw, rh = procesar_imagen(obtener_imagen(DIRECCION))
    mostrar_imagen(img, wi, hi, rw, rh)
