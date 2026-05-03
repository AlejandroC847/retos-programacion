# Ejercicio 10 - Código Morse

## Descripción

Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.

- Debe detectar automáticamente de qué tipo se trata y realizar
  la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
  o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
  <https://es.wikipedia.org/wiki/Código_morse.>

## Enfoque

Se implementa una función `nat_to_morse()` que recibe una cadena en texto
natural y la convierte en código morse.

Se implementa una función `morse_to_nat()` que recibe una cadena en código
morse y la convierte en texto natural.

Se implementa una función `is_morse()` que analiza la cadena de entrada para
determinar si el formato corresponde a código morse o a texto natural,
permitiendo así la conversión automática.

...

Se utilizan las siguientes tablas de conversion entre caracteres:

---

| Letra | Código  | Letra | Código  |
|-------|---------|-------|---------|
|   A   |· −      |   N   |− ·      |
|   B   |− · · ·  |   O   |− − −    |
|   C   |− · − ·  |   P   |· − − ·  |
|   D   |− · ·    |   Q   |− − · −  |
|   E   |·        |   R   |· − ·    |
|   F   |· · − ·  |   S   |· · ·    |
|   G   |− − ·    |   T   |−        |
|   H   |· · · ·  |   U   |· · −    |
|   I   |· ·      |   V   |· · · −  |
|   J   |· − − −  |   W   |· − −    |
|   K   |− · −    |   X   |− · · −  |
|   L   |· − · ·  |   Y   |− · − −  |
|   M   |− −      |   Z   |− − − ·  |

---

|      Signo      |     Código    |
|-----------------|---------------|
|Punto (.)        |· − · − · −    |
|Coma (,)         |− − · · − −    |
|Interrogación (?)|· · − − · ·    |
|Guion (-)        |− · · · · −    |
|Barra (/)        |− · · − ·      |

---

| Número  | Código  |
|---------|---------|
|    1    |· − − − −|
|    2    |· · − − −|
|    3    |· · · − −|
|    4    |· · · · −|
|    5    |· · · · ·|
|    6    |− · · · ·|
|    7    |− − · · ·|
|    8    |− − − · ·|
|    9    |− − − − ·|
|    0    |− − − − −|

## Estructura

codigo_morse.py → lógica principal
tests.py → pruebas básicas con assert y pytest

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
