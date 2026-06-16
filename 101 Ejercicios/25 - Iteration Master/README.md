# Ejercicio 25 - Iteration Master

## Descripción

Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.

## Enfoque

A continuación se explica el comportamiento de cada función para lograr imprimir
la secuencia de MIN a MAX (que por defecto estan establecidos en 1 y 100 respectivamente.)

### _get_sep()

Esta es la única función de la lista que no itera. Recibe un número,
determina si es el último de la sucesión y en ese caso retorna la cadena ".\n",
de lo contrario retorna la cadena ", ".
Llamaremos _separador_ al valor que retorne esta función.

### iteration_for()

Utiliza un bucle for sencillo con el rango de _MIN_ a _MAX_ para imprimir el número
con su respectivo separador.

### iteration_while()

Inicializa un num = _MIN_ y después un bucle que imprime el valor de num y luego
le suma 1. La condición del bucle es que num sea menor o igual a _MAX_.

### iteration_recursive()

Esta función con un argumento por defecto num = _MAX_ se llama a si misma, pasando
como argumento num - 1 y posteriormente imprime el numero con su separador.
Aprovecha la pila de llamadas para imprimir desde _MIN_ hacia _MAX_.

### iteration_list()

Genera una lista por medio de comprensión de lista. La compresión convierte cada
elemento del rango de _MIN_ a _MAX_ en una cadena, y le concatena su respectivo elemento.

Posteriormente genera una función personalizada a partir de la función `partial()`
proveniente de `functools` que recibe una función y argumentos; en este caso recibe
print y el argumento end="".

Finalmente mapea la lista generada con la función personalizada para imprimir cada
número con su separador sin saltos de linea.

### iteration_stdlib()

Usa el módulo `itertools` para obtener su clase `count` que genera un flujo
infinito empezando desde _MIN_.

Posteriormente usa la clase `slice` para detener el flujo en _MAX_ - _MIN_ + 1
para obtener la cantidad exacta de elementos del rango.

Finalmente se imprime una lista desempaquetada creada por medio de comprensión donde
recibe cada elemento del flujo y concatena su separador.

### iteration_class()

Se crea una clase `IteratorClass` que contiene un atributo num = _MIN_ - 1 y otro
max = _MAX_ que se inicializan en su método `init`.

Tiene los métodos mágicos `iter` y `next` que se encargan de la lógica para convertir
la clase en un objeto iterable. Dentro de `next`se establece que si
el atributo num es mayor o igual al atributo max entonces se lanza la
excepción controlada `StopIteration` sino el flujo continúa sumando 1 al
atributo num y retornando el valor.

Fuera de la clase se instancia ésta y se usa un bucle for simple que itera sobre
nuestra instancia, recibiendo e imprimiendo los valores del rango con su
separador respectivo.

### iteration_exec()

Crea una lista de cadenas por medio de comprensión y un rango de _MIN_a _MAX_,
donde cada cadena tiene la forma:

```python
"print(n, end=separador)\n"
```

Y donde n es el número de la sucesión y separador es el que corresponde.

Finalmente se unen todas las cadenas en un comando final que es pasado como
argumento a la función `exec()`.

### iteration_eval()

Crea una cadena de texto que representa a una lista por compresión con un rango
de _MIN_ a _MAX_, pero en vez de retornar solo el valor, se llama a print que recibe
como argumentos al número y end igual al separador respectivo.

Finalmente esa cadena completa se le pasa como argumento a la función `eval()`,
y adicionalmente de manera defensiva se pasa el argumento `globals()`
para evitar errores de alcance.

## Estructura

- iteration_master.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python iteration_master.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
