# Ejercicio 20 - Conversor Tiempo

## Descripción

Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.

## Enfoque

Se implementa una función `convert_time()` que recibe 4 parametros opcionales
con un valor por defecto de 0: `days`, `hours`, `mins` y `secs`.

El módulo tambien tiene la conversion de cada unidad a milisegundos por medio
de constantes. Cada argumento proporcionado se multiplica por el valor de la
constante que le corresponde para finalmente sumar los valores de cada unidad y
retornar el resultado de milisegundos equivalentes.

Si falta algun argumento, o no se pasa ninguno, al tener un valor por defecto
de 0, entonces se suma 0 al resultado final.

## Estructura

- conversor_tiempo.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python conversor_tiempo.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
