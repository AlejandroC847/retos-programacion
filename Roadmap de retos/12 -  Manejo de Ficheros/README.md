# Ejercicio 12 - Manejo de Ficheros

## Descripción

EJERCICIO:
Desarrolla un programa capaz de crear un archivo que se llame como
tu usuario de GitHub y tenga la extensión .txt.
Añade varias líneas en ese fichero:

- Tu nombre.
- Edad.
- Lenguaje de programación favorito.
Imprime el contenido.
Borra el fichero.

DIFICULTAD EXTRA (opcional):
Desarrolla un programa de gestión de ventas que almacena sus datos en un
archivo .txt.

- Cada producto se guarda en una línea del archivo de la siguiente manera:
  [nombre_producto], [cantidad_vendida], [precio].
- Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  actualizar, eliminar productos y salir.
- También debe poseer opciones para calcular la venta total y por producto.
- La opción salir borra el .txt.

## Enfoque

Se cambio la estructura del ejercicio. Primero si se realiza una función
`files_management` que ejemplifica la administracion de ficheros, tanto lectura
como escritura.

Posteriormente Se implementa una clase `SalesManager` para el ejercicio extra,
que ayuda a gestionar la base de datos de un inventario de una empresa.

La clase contiene los atributos:

- file: Es la ruta completa del archivo que se guardara como json de registros.
- products: Diccionario que almacena la informacion de los productos por medio
de diccionarios internos. Es el que contiene la información de todo el inventario.

Tambien contiene los siguientes métodos:

- _product_exist: Recibe el nombre de un producto. Si existe dentro del inventario
retorna `True`, de lo contrario retorna `False`.
- add_products: Recibe opcionalmente a manera de kwargs productos con formato
producto={"price": 0.0, "units_sold": 0}. Si se reciben argumentos se validan
y si son válidos se agregan al inventario. Si no se pasaron argumentos el usuario
puede agregarlos por consola manualmente.
- check_inventory: Imprime en pantalla una tabla con la informacion del inventario.
- update_product: Recibe un nombre de producto, un precio y una cantidad de unidades
vendidas, y si existe el producto se modifica su información.
- delete_product: Recibe un nombre de producto, si existe y se confirma la operación
se elimina el registro del inventario.
- clean_inventory: Despues de confirmar la operacion se limpia el inventario interno
de la clase y se elimina el archivo de registros.
- load_changes: Se llama al instanciar la clase, recupera la informacion del archivo
de registros si existe y la almacena en el diccionario interno de la clase. Si no
existe el archivo se inicializa el diccionario interno vacío.
- save_changes: Puede recibir un argumento `silent` opcional (por defecto es False)
para guardar la informacion del inventario interno en el archivo de registros si
el diccionario esta vacio, de lo contrario, se elimina el archivo de registros
(porque no hay registros). Finalmente se imprime un mensaje de finalización si
silent es `False`.

## Ejecución

### Ejecutar Programa

```bash
python manejo_de_ficheros.py
```

### Ejecutar Tests

```bash
python tests.py
```

o

```bash
pytest tests.py
```
