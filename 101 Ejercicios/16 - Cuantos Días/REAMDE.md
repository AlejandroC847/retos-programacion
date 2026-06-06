# Ejercicio 16 - Cuántos Días?

## Descripción

Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas.

- Una cadena de texto que representa una fecha tiene el formato "dd/mm/yyyy".
- La función recibirá dos String y retornará un int.
- La diferencia en días será absoluta (no importa el orden de las fechas).
- Si una de las dos cadenas de texto no representa una fecha correcta se
  lanzará una excepción.

## Enfoque

Se implementa una función `validar_fecha()` que recibe solo una cadena que
representa a la fecha en formato "dd/mm/yyyy". La función valida si se trata
de una fechade una cadena, si tiene exactamente 10 caracteres, si todos ellos
son numeros y barras divisorias en el orden correcto, y si las fechas representadas
tienen coherencia y validez. En caso de ser fechas validas retorna `True`, de lo
contrario retorna `False`.

Tambien se implementa una función `is_leap_year()` que recibe un numero entero
que representa un año y retorna `True` si se trata de un año bisiesto, o `False`
en caso contrario. Para ello comprueba que sea divisible entre 4, o si es
divisible entre 100 tambien lo sea entre 400.

Finalmente una función llamada `cuantos_dias()` se encarga de llamar a las
anteriores para recibir dos fechas, validarlas desde la fecha de inicio
"01/01/1582" y contar la cantidad de dias entre ellas.

## Estructura

- cuantos_dias.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python cuantos_dias.py
```

ó

```bash
python cuantos_dias.py fecha1 fecha2
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
