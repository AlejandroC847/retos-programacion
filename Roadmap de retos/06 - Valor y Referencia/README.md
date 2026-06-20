# Ejercicio 06 - Valor y Referencia

## Descripción

EJERCICIO:

- Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
  su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y
  "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
(Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como
variables anteriormente.

- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso,
por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y
  su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime
  el valor de las variables originales y las nuevas, comprobando que se ha invertido
  su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.

## Enfoque

Debido a la naturaleza del ejercicio se cambió el paradigma. No se presentaron
dos funciones para ejemplificar el paso por valor o por referencia, sino que se
creó una función que a manera de resumen explica textualmente los tipos de
datos inmutables y mutables en python (que provocan el efecto "por valor" y "por
referencia"). Se indica que tipos de datos son mutables, e inmutables y se ofrecen
un par de ejemplos de como se utilizan.

No se consideró necesario programar las funciones que reciban los parámetros por
valor y por referencia porque no es posible hacer eso, sino que si es por referencia
debe pasarse un valor mutable, y si es por valor debe pasarse uno inmutable o mutable
a partir de un constructor, lo cual se ejemplifico bien en la función integrada
y explicada anteriormente.

## Estructura

- valor_y_referencia.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python valor_y_referencia.py
```

### Ejecutar Tests

Este módulo no requiere de tests.
