"""
Módulo capaz de transformar texto natural a código morse y viceversa.

Reglas del Código Morse Internacional:

- El lenguaje natural solo acepta los siguientes caractere:
    - Letras, números y signos de puntuación basicos (' ', '.', ',', '?', '-' y '/')
- Sobre los espacios en el código morse:
    - Entre puntos y rayas del codigo no hay espacios para caracteres individuales.
    - Entre letras del código se utilizan espacios simples ' '.
    - Entre palabras del código se utilizan barras '/' o espacios dobles '  '.
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/04/23"

MORSE_DICT={
    #+Alfabeto
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "---.",
    #+Números
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    #+Símbolos
    "." : ".-.-.-",
    "," : "--..--",
    "?" : "..--..",
    "-" : "-....-",
    # Si es lenguaje natural, la barra se convierte al siguiente codigo,
    # si es codigo se convierte a espacio simple.
    "/" : "-..-.",
    #+ Espacio
    # Despues de cada caracter se agrega un espacio. Si el caracter es un espacio,
    # habra un total de dos espacios.
    " " : " "
}

NAT_DICT= {
    #+Alfabeto
    ".-" : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.." : "D",
    "." : "E",
    "..-." : "F",
    "--." : "G",
    "...." : "H",
    ".." : "I",
    ".---" : "J",
    "-.-" : "K",
    ".-.." : "L",
    "--" : "M",
    "-." : "N",
    "---" : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-." : "R",
    "..." : "S",
    "-" : "T",
    "..-" : "U",
    "...-" : "V",
    ".--" : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "---." : "Z",
    #+Números
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "-----" : "0",
    #+Símbolos
    ".-.-.-" : ".",
    "--..--" : "",
    "..--.." : "?",
    "-....-" : "-",
    "-..-." : "/",
    #+ Espacio
    "/" : " "
}

def nat_to_morse(texto: str) -> str:
    """Convierte texto natural en código morse.

    Args:
        texto (str): Cadena de texto en lenguaje natural.

    Returns:
        str: Cadena de texto traducida a código morse.
    """

    if not isinstance(texto, str):
        raise TypeError(
            f"Se esperaba una cadena de texto, pero se recibió {type(texto).__name__}"
            )

    texto = texto.upper()

    try:
        return " ".join(MORSE_DICT[char] for char in texto)
    except KeyError as exc:
        raise ValueError(
                        f"El texto '{exc.args[0]}' proporcionado Contiene caracteres inválidos."
        ) from exc

def morse_to_nat(codigo: str) -> str:
    """Convierte código morse en texto natural.

    Args:
        codigo (str): Cadena de texto en código morse.

    Returns:
        str: Cadena de texto traducida a lenguaje natural.
    """

    if not isinstance(codigo, str):
        raise TypeError(
            f"Se esperaba una cadena de texto, pero se recibió {type(codigo).__name__}"
            )

    texto_nat = []

    codigo = codigo.replace("   ", "/") # Convierte todos los espacios dobles en "/"
    palabras = codigo.split("/") # Separa la oracion por palabras

    for p in palabras:
        letras_morse = p.split()

        try:
            palabra_nat = "".join(NAT_DICT[letra] for letra in letras_morse)
            texto_nat.append(palabra_nat)
        except KeyError as exc:
            raise ValueError(
                            f"El codigo '{exc.args[0]}' proporcionado no coincide con morse. "
                            "Revisa que esté bien escrito."
            ) from exc

    return " ".join(s for s in texto_nat if s)

def is_morse(cadena: str) -> bool:
    """Evalúa si la cadena de texto es morse o lenguaje natural.

    Args:
        cadena (str): Texto original a evaluar.

    Returns:
        bool: Resultado de la evalación. True para morse. False para lenguaje natural.
    """

    if not isinstance(cadena, str):
        raise TypeError(
            f"Se esperaba una cadena de texto, pero se recibió {type(cadena).__name__}"
        )

    return all(c in ".-/ " for c in cadena)

# =========================
# Ejecución Principal
# =========================
if __name__ == "__main__":
    MSG_SOS= "Sos"
    MSG_HOLA = ".... --- .-.. .-/-- ..- -. -.. ---"

    print(morse_to_nat(m) if is_morse(m := MSG_HOLA) else nat_to_morse(m))
    print(morse_to_nat(m) if is_morse(m := MSG_SOS) else nat_to_morse(m))
