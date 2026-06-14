# Ejercicio 19 - Tres En Raya

## Descripción

Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
y retorne lo siguiente:

- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es
correcta o si han ganado los 2.

Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.

## Enfoque

Se implementa un funión llamada `evaluate_tic_tac_toe()` que se encarga de
verificar el estado de juego, recibe una matriz de juego y retorna si el ganador
fue 'X', si fue 'O', si fue empate, si el juego es nulo por movimientos inválidos
o si el juego aún no termina. Para que el programa no se rompa se valida al principio
el tablero de juego por medio de la función `is_valid_board_content()` que recibe
la matriz de juego y determina que los elementos de cada casilla solo sean "X",
"O" o una cadena de texto vacía, pero antes de eso llama a la función
`_validate_board_structure()` que verifica que la matriz sea una tupla conformada
por 3 tuplas que representan cada fila, y a su vez, cada fila es de 3 cadenas
de texto, donde cada una representa cada casilla de la matriz. Finalmente despues
de validar el que el contenido de la matriz sea válido en la función principal,
se verifica que se trate de un juego justo usando la función `is_fair_game()`
que verifica que la cantidad de movimientos sea justa, es decir, con una diferencia
menor o igual a 1 (por ejemplo 5 turnos para X y 4 para O, o 3 turnos para X y
3 turnos para O).

## Estructura

- tres_en_raya.py → lógica principal
- tests.py → pruebas básicas con assert y pytest

## Ejecución

### Ejecutar Programa

```bash
python tres_en_raya.py
```

### Ejecutar Tests

```bash
python tests.py
```

ó

```bash
pytest tests.py
```
