# Ejercicio 07 - Recursividad

## Descripción

EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.

DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:

- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la
  sucesión de Fibonacci (la función recibe la posición).

## Enfoque

Se implementó una función de prueba `recursivity()` que recibe un número entero,
por defecto igual a 100, e imprime todos los números desde ese número _n_ hasta 0.

Tambien se agrega una función `factorial()` que recibe un número entero no negativo
(por defecto es 0) y retorna el resultado de _n!_ por medio de llamadas recursivas
que multiplican sobre si los números desde 1 hasta _n_.

Por último se presenta la función `fibonacci()` que recibe un número entero no negativo
que indica la posición del elemento de la serie fibonacci que va a retornar.
Para ello usa llamadas recursivas de la función con los argumenos _n - 1_ y
_n - 2_ hasta llegar a _n = 1_ devolviendo 0 y _n = 2_ devolviendo 1.

## Estructura

- recursividad.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python recursividad.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
