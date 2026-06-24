# Ejercicio 08 - Pilas y Colas

## Descripción

EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de
las pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura
de array o lista (dependiendo de las posibilidades de tu lenguaje).

DIFICULTAD EXTRA (opcional):

- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de
  la web. Las palabras "adelante", "atrás" desencadenan esta acción, el resto se
  interpreta como el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de
  una impresora compartida que recibe documentos y los imprime cuando así se le indica.
  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  interpretan como nombres de documentos.

## Enfoque

Se implementan 3 funciones para cada estructura (LIFO y FIFO) que ejecutan las
siguientes acciones:

- **add_element**: Inserta un elemento al final de la estructura
- **pop_element**: Extrae un elemento de la estructura. El primero si es FIFO y
el último si es LIFO. El elemento extraido se retorna y es eliminado de la estructura.
- **drain**: Extrae todos los elementos de la estructura (de izquierda derecha
si es FIFO, o a la inversa si es LIFO) y retorna una lista con los elementos extraidos.

Tambien se implementan dos funciónes con ejemplos practicos:

- **nav_web**: Simula el comportamiento del historial de un navegador, permitiendo
ir hacia adelante o hacia atras en el historial guardando el registro de los sitios
en los que se navega (LIFO).
- **printer**: Simula el comportamiento de una cola de impresión de una impresora.
Permite agregar mas elementos al final de la cola de impresión, o imprimir el
primer elemento que se encuentre en la cola de impresión.

## Estructura

- pilas_y_colas.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python pilas_y_colas.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
