# Ejercicio 03 - La Sucesión de Fibonacci

## Descripción

* Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
  * La serie Fibonacci se compone por una sucesión de números en la que el
  siguiente siempre es la suma los dos anteriores.
* Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13...

---

## Enfoque

Se implementan dos funciones alternativas que reciben como parámetro un valor
entero **_n_**, calcúlan el número correspondiente a esa posición dentro de la
sucesión y lo retornan.

* `fibonacci_v1(n: int)` utiliza recursión siguiendo el planteamiento original
de la serie, lo que la vuelve ineficiente.
* `fibonacci_v2(n: int)` utiliza un bucle para sumar los dos valores previos
en cada iteración, retornando al final el valor de la n-ésima posición.

Posteriormente en una función `print_fibonacci()` se imprimen un título y por
medio de un bucle los 50 primeros números de la serie llamando a la
función `fibonacci_v2(n: int)`.

---

## Estructura

* `sucesion_fibonacci.py` → lógica principal
* `tests.py` → pruebas básicas con `assert`

---

## Ejecución

### Ejecutar Programa

```bash
python sucesion_fibonacci.py
```

### Ejecutar Tests

```bash
python tests.py
```
