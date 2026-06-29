# Ejercicio 11 - Excepciones

## Descripción

EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.

- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.

## Enfoque

Se implementa una función informativa que explica las excepciones mas comunes
en el lenguaje. Muestra una a una su nombre, una breve descripción y un ejemplo
de ejecución.

También se crea una excepción personalizada que puede recibir dos argumentos
(un código de error y un mensaje de error)

Finalmente una función de prueba recibe argumentos y es capaz de lanzar dos
excepciones built-in (TypeError y ValueError) y la excepcion personalizada.

## Ejecución

### Ejecutar Programa

```bash
python excepciones.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
