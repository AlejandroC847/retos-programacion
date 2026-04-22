# Ejercicio 08 - Contando Palabras

## Descripción

Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.

- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
  lo resuelvan automáticamente.

## Enfoque

Se implementa una función `contar_palabras()` que recibe una cadena de texto,
cuenta cuantas palabras tiene (separandolas con cualquier caracter no alfanumerico)
y va creando un diccionario en el que las claves son las palabras encontradas
y los valores son la frecuencia de cada palabra. Por ultimo se retorna el diccionario.

Adicionalmente una función `mostrar_diccionario()` permite imprimir a manera
de lista las palabras seguidas de su frecuencia.

## Estructura

- aspect_ratio.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python contando_palabras.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytests tests.py -v
```
