# Ejercicio 03 - Funciones y Alcance

## Descripción

- Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número
  en lugar de los textos.

## Enfoque

Este módulo explora el uso de funciones en el lenguaje, cubriendo desde su sintaxis
básica hasta conceptos avanzados de alcance (scope):

### Tipos de funciones

- Sin parámetros
- Con parámetros (incluyendo *args)
- Con retorno
- Funciones anidadas.

### Gestión de variables

Diferencia entre variables locales y globales.

### Funciones integradas

Uso de herramientas propias del lenguaje.

Incluye una demostración práctica para visualizar cómo el código gestiona el
entorno y las variables dentro de las funciones.

### Ejercicio final

Se ha implementado una función que procesa dos cadenas de texto y recorre los
números del 1 al 100.

El programa clasifica cada número según sus divisores
(múltiplos de 3, de 5, o de ambos) y muestra el resultado en pantalla, devolviendo
finalmente la cuenta total de los números que no cumplieron ninguna de estas condiciones.

## Estructura

- funciones_alcance.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python funciones_alcance.py
```

### Ejecutar Tests

Este módulo no requiere de test.
