# Ejercicio 17 - En Mayúscula

## Descripción

Crea una función que reciba un String de cualquier tipo y se encargue de
poner en mayúscula la primera letra de cada palabra.

## Enfoque

Se implementa una función `first_mayus()` que recibe una cadena de texto, la
recorre caracter por caracter y cuando detecta que se trata la inicial de una
palabra (por medio de una bandera `is_first_letter`) la cambia a mayúscula si
es una letra minúscula, de lo contrario conserva el caracter original.
Finalmente retorna la cadena modificada.

## Estructura

- en_mayuscula.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python en_mayuscla.py
```

ó

```bash
python en_mayuscula.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
