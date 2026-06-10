# Ejercicio 18 - La Carrera De Obstáculos

## Descripción

Crea una función que evalúe si un/a atleta ha superado correctamente una
carrera de obstáculos.

- La función recibirá dos parámetros:

  - Un array que sólo puede contener String con las palabras "run" o "jump"
  - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)

- La función imprimirá cómo ha finalizado la carrera
  - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será
  correcto y no variará el símbolo de esa parte de la pista.
  - Si hace "jump" en "_" (suelo), se variará la pista por "x".
  - Si hace "run" en "|" (valla), se variará la pista por "/".

- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.

## Enfoque

Se implementa una función `start_race()` que recibe dos parámetros, la
pista (str) y las acciones del atleta (list[str]), posteriormente llama a una
función `validate_track()` que recibe la cadena de texto de la pista y valida
que tenga el formato adecuado, solo con caracteres "_" y "|"; si es válida retorna
True y continua la ejecución, de lo contrario retorna False y se lanza una
excepción `ValueError`. Posteriormente se llama a la función `validate_actions()`
que valida el formato de las acciones; éstas deben ser una lista de string,
y cada elemento debe ser "run" o "jump" solamente, si la validación es exitosa
retorna True y el programa continúa, de lo contrario retorna False y se lanza
una excepción `ValueError`. Si no se pasan los argumentos con el tipo adecuado,
entonces se lanzará una excepción `TypeError`. Si todo transcurre con normalidad
compara las acciones con la pista, guarda los resultados con "x" para errores
y "/" para aciertos para posteriormente imprimirlos gracias a la función `print_race_summary()`.
Finalmente si solo obtuvo aciertos la función `start_race()` retorna True
simbolizando una carrera perfecta, de lo contrario retorna False.

## Estructura

- carrera_obstaculos.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python carrera_obstaculos.py
```

ó

```bash
python carrera_obstaculos.py "pista" accion1 accion2 accion3 ...
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
