# Ejercicio 02 - Es un anagrama?

## Descripción

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.

- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.

---

## Enfoque

Se implementa una función `is_anagram(word_1, word_2)` que determina si una
palabra es anagrama de la otra y devuelve el resultado correspondiente como
valor lógico (booleano).

Luego, se utiliza una función `evalue_anagram()` para solicitar las palabras
por medio de la entrada del usuario y retornar la respuesta.

---

## Estructura

- `es_un_anagrama.py` → lógica principal
- `tests.py` → pruebas básicas con `assert`

---

## Ejecución

### Ejecutar programa

``` bash
python es_un_anagrama.py
```

### Ejecutar tests

```bash
python tests.py
