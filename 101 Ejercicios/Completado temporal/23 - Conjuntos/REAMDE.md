# Ejercicio 23 - Conjuntos

## Descripción

Crea una función que reciba dos array, un booleano y retorne un array.

- Si el booleano es verdadero buscará y retornará los elementos comunes
  de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes
  de los dos array.
- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.

## Enfoque

Se implementa una función `sets()` que recibe dos listas y un booleano como argumentos
opcionales. Las primeras dos son conjuntos de elementos, mientras que el booleano
es el argumento `find_common` que, si es _True_ se realiza una intersección entre
conjuntos, pero si es False se realiza una diferencia simétrica de los conjuntos.

Finalmente se retorna una lista con los elementos obtenidos de la operacion realizada.

## Estructura

- conjuntos.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python conjuntos.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
