# Ejercicio 24 - Máximo Común Divisor y Mínimo Común Múltiplo

## Descripción

Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
que calcule el mínimo común múltiplo (mcm) de dos números enteros.

- No se pueden utilizar operaciones del lenguaje que
  lo resuelvan directamente.

## Enfoque

Se hace uso del siguiente algoritmo para obtener el _MCD_.

### Algoritmo de Euclides

#### ¿Cómo funciona?

El algoritmo se basa en realizar divisiones sucesivas. La premisa fundamental
es que el MCD de dos números no cambia si el número mayor se reemplaza por el
residuo de su división entre el menor.

#### Proceso paso a paso

- Divide el número mayor (A) entre el número menor (B).
Esto te dará un cociente (C) y un residuo (R). Es decir: A = B ⋅ C + R.
Si el residuo R es 0, entonces el MCD es el divisor B.
- Si el residuo R no es 0, convierte a B en el nuevo dividendo y a R en
el nuevo divisor.
- Repite la división.
- Continúa con este ciclo hasta obtener un residuo de cero.

El último residuo que no sea cero será el MCD de tus dos números originales.

Por otro lado el _mcm_ de dos números siempre es igual a su producto
dividido entre su Máximo Común Divisor (_MCD_).

Se implementa una función `mcd()` que recibe dos argumentos de tipo entero que
serán los valores _a_ y _b_, a los cuales se les aplicara el algoritmo de euclides
para finalmente retornar su _MCD_.

También se implementa una función  `mcm()` que de igual manera recibe dos argumentos
de tipo entero y usa la propiedad fundamental en la teoría de números de dividir
el producto de los argumentos sobre el _MCD_ de los mismos, obteniendo y retornando
el valor del _mcm_.

## Estructura

- mcd_y_mcm.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python mcd_y_mcm.py
```

o

```bash
python mcd_y_mcm.py num_a num_b
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
