"""
Cuenta la frecuencia de cada palabra dentro de una cadena siguiendo las siguientes reglas:
- No es sensible a mayúsculas
- Si hay diferencia entre letras con y sin acentos.
- Los signos de puntuacion no forman parte de la palabra, se vuelven separadores de palabras:
    * Son dos palabras: 'don't', '10.5', '17/04', 't-rex'.
- Una "palabra" en realidad es un token que puede contener elementos alfanumericos y no
  no necesariamente tener significado real. Algunos ejemplos de palabras son "ABC", "Y2K", "2026"
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/17"

def contar_palabras(cad: str) -> dict:
    """Cuenta la frecuencia de las palabras dentro de una cadena

    Args:
        cad (str): Cadena de texto original

    Returns:
        dict: Diccionario con los valores (palabra, frecuencia). Por ejemplo: {"Rata" : 5}
    """
    if not isinstance(cad, str):
        raise TypeError("El argumento debe ser una cadena")

    if cad == "":
        raise ValueError("La cadena no puede estar vacía")

    cad = cad.lower() + "." #Punto ayuda para no cortar bucle antes de agregar la ultima palabra

    frecuencias = {}
    token = ""

    for c in cad:
        if c.isalnum():
            token += c
        else:
            if token != "":
                frecuencias[token] = frecuencias.get(token, 0) + 1

                token = ""

    if not frecuencias:
        raise ValueError("Cadena sin elementos alfanumericos")

    return frecuencias

def mostrar_diccionario(dic: dict, cad: str = ""):
    """Muestra el diccionario a manera de frecuencias por clave.

    Args:
        dic (dict): Diccionario de frecuencias.
        cad (str): Cadena de encabezado opcional, por defecto no se muestra.
    """

    if not dic:
        print("NO HAY NADA QUE MOSTRAR...")
        return

    if cad != "":
        print(f"FRASE ORIGINAL:\n{cad}")

    for i, (k, v) in enumerate(dic.items(), start=1):
        print(f"{i}. '{k}': Aparece {v} veces.")

# ====================
# Ejecución Principal
# ====================
if __name__ == "__main__":
    CADENA = "El Papa come papa, pero mi papá no come papa."
    dict_cad = contar_palabras(CADENA)
    mostrar_diccionario(dict_cad, CADENA)
