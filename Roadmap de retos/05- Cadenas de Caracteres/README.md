# Ejercicio 05 - Cadenas de Caracteres

## Descripción

EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):

- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
  recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
  interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:

- Palíndromos
- Anagramas
- Isogramas

## Enfoque

Se implementa una función de prueba `demo_str()`que contiene todas las operaciones
disponibles para los `str`.

Se implementan 3 funciónes que trabajan con cadenas y usan sus operaciones
en sus algoritmos:

- is_anagram(): Recibe dos cadenas y determina si son un anagrama. Retorna una
tupla con el valor booleano de la evaluación y un mensaje de respuesta
respecto al estatus.
- is_palindrome(): Recibe una cadena y determina si es un palíndromo.
Retorna el valor booleano de la evaluación.
- is_isogram(): Recibe una cadena y determina si es un isograma.
Retorna el valor booleano de la evaluación.

## Estructura

- cadenas_de_caracteres.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python cadenas_de_caracteres.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
