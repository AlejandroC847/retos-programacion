"""
Invertidor de cadenas. Recibe una cadena e intercambia el orden
de sus caracteres para mostrarla invertida.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/16"

def invertir_cadena(cad: str) -> str:
    """Invierte el orden de los caracteres de una cadena.

    Args:
        cad (str): Cadena original.

    Returns:
        str: Cadena invertida.
    """

    lista_caracteres = []

    for i in range(len(cad) - 1, -1, -1):
        lista_caracteres.append(cad[i])

    #Alternativa
    #for c in cad:
    #    lista_caracteres.insert(0, c) # Menos eficiente

    return "".join(lista_caracteres)

def mostrar_cadena(cad: str, msg: str = ""):
    """Imprime en pantalla la cadena recibida y el mensaje opcional.

    Args:
        cad (str): Cadena a imprimir.
        msg (str): Mensaje adicional previo. Por defecto es "".
    """

    print(f"{msg}{cad}")

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    mostrar_cadena(invertir_cadena("Hola tonotos"), "Cadena invertida: ") # sotonot aloH
