# Ejercicio 15 - Es un Número de Armstrong?

## Descripción

Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.

Un número de Armstrong (también conocido como número narcisista) es aquel que
es igual a la suma de sus propios dígitos, cada uno elevado a la potencia del
número total de dígitos de dicha cifra.

### La Regla Matemática

Para un número de $n$ dígitos, cada dígito $d_i$ debe elevarse a la potencia $n$.
El número es un número de Armstrong si se cumple que:
$$d_1^n + d_2^n + ... + d_n^n = \text{Número original}$$

## Enfoque

Se implementa una fucnión `is_armstrong()` que recibe un número entero no negativo.
Si no es entero lanza un `TypeError`, si es negativo lanza un `ValueError`.
Posteriormente convierte en _string_ el número ingresado (para manejar cada
caracter como digitos) y realiza la sumatoria de cada digito elevado a la
potencia de la cantidad total de digitos. Si el número resultante es igual al
número ingresado retorna _True_ de lo contrario retorna _False_.

## Estrcutura

- es_un_numero_de_armstrong.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python es_un_numero_de_armstrong.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
