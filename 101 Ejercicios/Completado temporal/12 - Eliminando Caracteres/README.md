# Ejercicio 12 - Eliminando Caracteres

## Descripción

Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).

- out1 contendrá todos los caracteres presentes en la str1 pero NO
  estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
  estén presentes en str1.

## Enfoque

Se implementa una funcion `eliminando_caracteres()` que recibe dos cadenas,
itera sobre cada una de ellas y elimina los caracteres que se encuentran en la
cadena opuesta, dejando un conjunto ordenado y no repetido. Finalmente retorna
una tupla con las cadenas resultantes.

Se implementa una función `filtrar_caracteres()` que recibe dos cadenas, itera
sobre cada una de ellas y elimina los caracteres que se encuentran en la cadena
opuesta, manteniendo la cadena original y su orden, pero sin los caracteres
de la cadena opuesta. Finalmente retorna una tupla con las cadenas resultantes.

## Estructura

- eliminando_caracteres.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python eliminando_caracteres.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
