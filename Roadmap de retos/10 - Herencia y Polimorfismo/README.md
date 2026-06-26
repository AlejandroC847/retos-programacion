# Ejercicio 10 - Herencia y Polimorfismo

## Descripción

EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.

DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.

## Enfoque

Se establecen dos ejemplos para demostrar el uso de la herencia y el polimorfismo.

### Animales

Se implementa una clase padre `Animal` que podria recibir una cadena de texo con
el nombre del animal, asignandolo como atributo.
Tambien se crean las clases hijas `Gato`, `Perro` y `Conejo`, todas ellas al
instanciarse establecen el atributo de nombre con el respectivo a su especie.
Ademas gracias a polimorfismo todas tienen el método `sonido()` que imprime en pantalla
un texto que simula el sonido que hace cada animal.

### Empresa

Se implementa una clase padre `Empleado` que debe recibir un nombre y un id en
formato cadena. Ambos argumentos se establecen como atributos al instanciar la
clase y se crea tambien el atributo `empleados_a_cargo`, que es una lista de
los empleados que tiene a cargo este empleado. Posee tambien el método mágico
`__str__()` que retorna una cadena formateada con el nombre, cargo, id y empleados
a cargo del empleado que se quiere imprimir.
Otros métodos presentes en la clase padre son `_puede_emplear()` que por defecto
retorna False, `emplear()` que recibe un empleado como argumento y llama a `_puede_emplear()`
y si tiene permiso lo agrega a la lista `empleados_a_cargo`; y por ultimo, el
método `despedir()` recibe un empleado como argumento, y si existe en la lista
`empleados_a_cargo` lo remueve de esta.

Posteriormente se instancian las siguientes clases hijas:

- `Gerente`: Tiene un método interno `_puede_emplear()` que retorna True, y un
método exvlusivo `tomar_decision_estrategica()` que recibe un str con la decisión
y simula al gerente tomandola.
- `LiderProyecto`: Tiene un método interno `_puede_emplear()` que retorna True,
y un método exvlusivo `planificar_proyecto()` que recibe el nombre del nuevo proyecto
y simula al lider de proyecto planificandolo.
-`Programador`: No tiene el método `_puede_emplear()` por lo que no se le pueden
agregar empleados a su cargo. Tiene el método exclusivo `escribir_codigo()` que
recibe el nombre del proyecto en el que trabajara y simula que lo hace.

## Ejecución

### Ejecutar Programa

```bash
python herencia_y_polimorfismo.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
