# Ejercicio 11 - Expresiones Equilibradas

## Descripción

Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.

- Equilibrado significa que estos delimitadores se abren y cieran
  en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
  No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ] - 5 )

## Enfoque

Se implementa una función `is_balanced()` que recibe una cadena de texto,
se espera una expresión matemática, evalúa si sus signos de agrupacion estan
equilibrados y en el orden correcto. Finalmente retorna el valor de la evaluación.

## Estructura

- expresiones_equilibradas.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python codigo_morse.py
```

### Ejecutar Pruebas

```bash
pytest tests.py
```

ó

```bash
pytest tests.py -v
```
