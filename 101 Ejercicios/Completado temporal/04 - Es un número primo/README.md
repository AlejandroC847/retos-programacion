# Ejercicio 04 - Es un número primo?

## Descripción

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

---

## Enfoque

Se implementa una función `prime_number()` que recibe como parámetro un número
natural (entero positivo). A partir del número determina si se trata de un
número primo o no. Si se trata de un número primo retorna True, si no es primo
retorna False, y si es un valor inválido retorna None.

Tambien hay una función adicional `print_prime_numbers()` que solicita al usuario
un número y por medio de la función `prime_number()` le indica si es primo o no.

Finalmente, otra función llamada `print_from_1_to_100()` se encarga de imprimir
todos los números primos dentro de un rango que por defecto es entre 1 y 100.

---

## Estructura

* `sucesion_fibonacci.py` → lógica principal
* `tests.py` → pruebas básicas con `assert`

---

## Ejecución

### Ejecutar Programa

```bash
python numero_primo.py
```

### Ejecutar Tests

```bash
python tests.py
```
