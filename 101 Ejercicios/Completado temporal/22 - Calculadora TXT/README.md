# Ejercicio 22 - Calculadora .TXT

## Descripción

Lee el fichero "entradas_calculadora.txt", calcula su
resultado e imprímelo.

- El .txt se corresponde con las entradas de una calculadora.
- Cada línea tendrá un número o una operación representada por un
  símbolo (alternando ambos).
- Soporta números enteros y decimales.
- Soporta las operaciones suma "+", resta "-", multiplicación "*"
  y división "/".
- El resultado se muestra al finalizar la lectura de la última
  línea (si el .txt es correcto).
- Si el formato del .txt no es correcto, se indicará que no se han
  podido resolver las operaciones.

## Enfoque

Se implementa una función llamada `calc_txt()` encargada de realizar los calculos
por medio de la cadena de texto. Para ello recibe como argumento una cadena de
texto con el nombre del archivo para posteriormente llamar a la función `read_file()`
que recibe el nombre como argumento y busca el archivo dentro de la carpeta actual.
Posteriormente si existe lee su contenido y lo retorna a manera de lista de
caracteres que incluye operandos y operadores idealmente.

Al recibir la lista, la función principal la convierte a una sola cadena de texto
y llama a `validate_expression()` pasandole la expresion en texto como argumento.
Esta revisa que tenga la sintaxis y contenido correcto; es decir, que solo
contenga números validos y operadores.

Si la validación es existosa el programa continua con el calculo de la expresion
parte por parte, por lo que el resultado es un calculo lineal, sin jerarquia de operaciones.

Finalmente retorna una tupla que contiene la expresion en texto y el
resultado final del calculo.

Adicionalmente se integra una función `write_file()` que recibe una cadena de texto
(que contiene una ruta de archivo txt) y una lista de strings que corresponde a
cada elemento de la expresion a insertar (números y operadores), para finalmente
escribir en el archivo cada parte de la expresión linea por linea.

## Estructura

- calculadora_txt.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python calculadora_txt.py
```

o

```bash
python calculadora_txt.py numero operador numero operador numero ...
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
