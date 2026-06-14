# Ejercicio 21 - Parando El Tiempo

## Descripción

Crea una función que sume 2 números y retorne su resultado pasados
unos segundos.

- Recibirá por parámetros los 2 números a sumar y los segundos que
  debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma
  asíncrona, es decir, sin detener la ejecución del programa principal.
  Se podría ejecutar varias veces al mismo tiempo.

## Enfoque

Se implementa una función asíncrona `stop_time()` que recibe 2 argumentos enteros
o flotantes: Un número _a_, un número _b_ y una cantidad _await_time_ para el
tiempo de espera.

La función se declara asíncrona por medio de _async_ y dentro hace uso de
`asyncio.sleep(await_time)` que "detiene" la ejecución de la función por durante
la cantidad de segundos que indica el valor de _await_time_.
Finalmente retorna la suma de los números _a_ y _b_.

Para usar de forma asíncrona multiples ejecuciones de la funcion se hace uso de
`asyncio.create_task(stop_time(*values))` y en ese instante la función se ejecuta
en segundo plano sin interferir en el flujo actual del programa, finalmente
se obtiene el valor que retorna usando _await_, haciendo que espere a que la
función `stop_time()` termine su ejecución (incluyendo su tiempo de espera).

## Estructura

- parando_el_tiempo.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python parando_el_tiempo.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
