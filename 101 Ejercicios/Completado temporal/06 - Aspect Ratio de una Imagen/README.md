# Ejercicio 06 - Aspect Ratio de una Imagen

## Descripción

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.

- Url de ejemplo:
    <https://i.pinimg.com/736x/22/21/12/222112c36704f8e08011c7c2da22c8f9.jpg>
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.

## Enfoque

Se implementa una función `obtener_imagen()` que recibe un str con una url, de
ella extrae el contenido solo si se trata de una imagen y lo retorna como bytes.
Posteriormente otra función llamada `procesar_imagen()` recibe el contenido de
bytes y lo transforma a una imagen real, obteniendo sus medidas y su ratio de aspecto,
retornando la imagen procesada (y reescalada para ajustarla a la pantalla), las
dos medidas y los dos valores de su ratio.
Finalmente y de manera opcional una función `mostrar_imagen()` crea una ventana
de tkinter donde presenta la imagen con sus datos debajo.

## Estructura

- `aspect_ratio.py` → lógica principal
- `tests.py` → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python aspect_ratio.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
