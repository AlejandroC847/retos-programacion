# Ejercicio 09 - Clases

## Descripción

EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)

- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.

## Enfoque

Se implementan 3 clases, una de ejemplo `Example` junto a una función para mostrar
como instanciar un objeto de la clase, como recibir parametros, crear atributos
y crear métodos.

Otra clase `Stack` contiene un atributo de tipo lista para representar a la pila,
puede recibir argumentos que seran elementos de esa pila y los métodos permiten
agregar elementos, extraer uno o extraer todos, siguiendo el paradigma LIFO.
Ademas se establece un metodo encapsulado como property para retornar el tamaño
de la pila y el metodo `__str__` que permite imprimir directamente la pila y
sus elementos usando `print()`.

Por último una clase `Queue` contiene un atributo de tipo lista para representar
a la cola, puede recibir argumentos que seran elementos de esa cola y los métodos
permiten agregar elementos, extraer uno o extraer todos, siguiendo el paradigma FIFO.
Ademas se establece un metodo encapsulado como property para retornar el tamaño
de la cola y el metodo `__str__` que permite imprimir directamente la cola y sus
elementos usando `print()`.

## Ejecución

### Ejecutar Programa

```bash
python clases.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
