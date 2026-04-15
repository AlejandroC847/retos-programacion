# Ejercicio 05 - Área de un polígono

## Descripción

Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.

- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.

## Enfoque

Se implementa el concepto de polimorfismo creando una clase base abstracta `Poligono`.
De ésta heredan otras clases que representan diferentes polígonos:

- `Triangulo`
- `Cuadrado`
- `Rectangulo`
- `Trapecio`
- `Rombo`
- `PoligonoRegular`

Dentro de todas las clases se encuentra el método `calcular_area()`, que funciona
diferente dependiendo del polígono que se trabaje, pero siempre retorna el resultado.

Finalmente existe una función llamada `imprimir_area()`que recibe como parámetro
un `Poligono` hijo, no la clase base e imprime en pantalla el nombre del
polígono, sus medidas y su área.

## Estructura

- `area_poligono.py` → lógica principal
- `tests.py` → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

`bash
python area_poligono.py
`

### Ejecutar Tests

`bash
python tests.py
`
ó
`bash
pytest tests.py -v
`
