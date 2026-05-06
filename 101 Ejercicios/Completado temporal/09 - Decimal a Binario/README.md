# Ejercicio 09 - Decimal a Binario

## Descripción

Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

## Enfoque

Se implementa una función `dec_a_bin()`que recibe un número entero positivo.
El número decimal es convertido a binario por medio del método de divisiones sucesivas.
Finalmente retorna una lista con
cada bit del número convertido a binario.

Tambien se implementa una función alternativa `lista_bin_a_str()` que recibe
una lista (idealmente de bits pero funciona con cualquiera) y convierte cada
elemento en cadenas de texto, las concatena y retorna el número binario de tipo str.

## Estructura

- aspect_ratio.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python decimal_a_binario.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py -v
```
