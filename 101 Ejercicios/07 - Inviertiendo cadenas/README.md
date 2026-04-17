# Ejercicio 07 - Invirtiendo cadenas

## Descripción

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

## Enfoque

Se implementa una función llamada `invertir_cadena()` que recibe como parámetro
una cadena (str) para despues retornar una cadena invertida (str) con el mismo
contenido que la original pero con sus caracteres en orden inverso.

Posteriormente se hace uso de una función `mostrar_cadena` que recibe dos parámetros.

- El primero es la cadena principal que se imprimirá en consola.
- El segundo, que es opcional, permite añadir un mensaje antes de la primer cadena,
por defecto esta vacía.s

## Estructura

- aspect_ratio.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

`bash
python invirtiendo_cadenas.py
`

### Ejecutar Tests

`bash
python tests.py
`
ó
`bash
pytest tests.py -v`
