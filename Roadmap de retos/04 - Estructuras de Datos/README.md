# Ejercicio 04 - Estructuras de Datos

## Descripción

### EJERCICIO

- Muestra ejemplos de creación de todas las estructuras soportadas por defecto
  en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.

### DIFICULTAD EXTRA (opcional)

Crea una agenda de contactos por terminal.

- Debes implementar funcionalidades de búsqueda, inserción, actualización
  y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
  y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no numéricos y con más
  de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.

## Enfoque

Se manejan las estructuras de datos nativas y las mas comunes de uso avanzado por
parte de la libreria `collections`.

Para cada estructura se realizo una función que dentro contiene los métodos
caracteristicos de la respectiva estructura. Finalmente se imprime en pantalla
la estructura.

Para obtener información útil acerca de cada estructura es recomendable revisar
el codigo para ver individualmente cada método.

## Estructura

- estructuras_de_datos.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python estructuras_de_datos.py
```

### Ejecutar Tests

Este módulo no requiere de test.
