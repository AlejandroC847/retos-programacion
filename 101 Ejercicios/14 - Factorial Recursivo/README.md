# Ejercicio 14 - Factorial Recursivo

## Descripción

Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.

## Enfoque

Se implementa una función `factorial_recursivo()` que recibe un número entero
positivo _n_. Posteriormente calcula el factorial del número (_n!_) por medio
de multiplicar el número _n_ por el factorial de `n - 1` llamando a la misma
función (recursividad) hasta llegar a _n_ =  1 (o 0 según sea el caso) de modo
que se termina la recursion y va retornando los resultados de la multiplicacion.
La primer llamada a `factorial_recursivo()` finalmente retorna el valor
de _n_! como número natural.  

## Estructura

- factorial_recursivo.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python factorial_recursivo.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
