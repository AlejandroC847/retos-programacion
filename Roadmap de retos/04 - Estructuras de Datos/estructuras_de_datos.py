"""Módulo de demostración para estructuras de datos básicas y avanzadas:
- lista
- tuplas
- str
- rangos
- diccionarios
- sets
- frozenset
- bytes
- bytearray
- deque
- namedtuple
- counter
- defaultdict
"""
__author__ = "Alejandro Cortés"
__date__ = "2026/06/17"

import os
from collections import deque, namedtuple, Counter, defaultdict

#pylint: disable=pointless-statement

def _clear_console():
    """Limpiar la consola"""
    os.system("cls" if os.name == "nt" else "clear")

def _enter_to_continue():
    """Presionar enter para continuar"""
    input("Presione enter para continuar...")

def basic_sec_lista():
    """Listas (list): Mutables, ordenadas, permiten duplicados."""

    mi_lista = ["Pato"]
    lista_2 = ["Kiwi", "Casuario", "Aguila"]

    # Inserción
    mi_lista.append("Ganzo")    # Al final
    mi_lista.insert(0, "Pato")  # En una posición específica
    mi_lista.extend(lista_2)    # Todos los elementos al final

    # Actualización y busqueda
    mi_lista[2] = "Pollo"       # Cambiar valor por índice
    mi_lista.index("Casuario")  # Busca el indice del elemento indicado
    mi_lista.reverse()          # Invierte el orden de la lista in-place. Método de listas
    reversed(mi_lista)          # Retorna lista invertida. Función integrada en python.

    # Borrado
    mi_lista.remove("Pato")     # Por valor (el primero en encontrarse)
    del mi_lista[0]             # Por índice
    mi_lista.pop()              # Recibe indice, ultimo valor por defecto. Retorna el valor borrado
    # mi_lista.clear()          # Borra toda la lista.

    # Ordenación
    mi_lista.sort()             # Ordenar alfabéticamente. Método de las listas.
    sorted(mi_lista)            # Retorna lista ordenada. Función integrada en python.

    mi_lista.copy()             # Retorna una copia de la lista original, no es una referencia.
    mi_lista.count("Pato")             # Cuenta los elementos especificados que tiene la lista.

    print(f"Lista final: {mi_lista}")

def basic_sec_tuplas():
    """Tuplas (tuple): Inmutables, ordenadas, permiten duplicados."""

    mi_tupla = ('A', 'B', 'C', 'D', 'E')

    mi_tupla.index("C")     # Busca el indice del elemento indicado
    mi_tupla.count("A")     # Cuenta los elementos especificados que tiene la lista.

    print(f"Tupla final: {mi_tupla}")

def basic_sec_str():
    """String (str): Inmutables, permiten cualquier caracter unicode y los duplicados."""

    cadena = "Texto"

    # Transformación de formato
        # Estos métodos devuelven una versión modificada del texto.

    cadena.upper()              # Convierte todo a mayúsculas o minúsculas.
    cadena.lower()              # Convierte todo a mayúsculas o minúsculas.

    cadena.capitalize()         # Pone en mayúscula solo la primera letra.

    cadena.title()              # Pone en mayúscula la primera letra de cada palabra.

    cadena.strip()              # Elimina los espacios en blanco al inicio y al final
    cadena.lstrip()             # Elimina los espacios en blanco al inicio (izquierda)
    cadena.rstrip()             # Elimina espacios en blanco al final (derecha)
    # Por defecto quitan saltos de línea, tabulaciones, retornos de carro o espacios.
    # Pero se puede pasar una cadena como argumento para ahora eliminar el contenido.

    cadena.replace("to", "as")  # Reemplaza una subcadena por otra.

    # Búsqueda y Validación
        # Devuelven un booleano o un índice.

    cadena.find("s")            # Busca la posicion de una subcadena (-1 si no lo encuentra)
    cadena.index("x")           # (lanza error si no lo encuentra)

    cadena.startswith("t")      # Verifican si el string comienza o termina con un texto dado.
    cadena.endswith("o")        # Verifica si el string termina con un texto dado.

    cadena.isdigit()            # Valida si el contenido son solo números
    cadena.isalpha()            # Valida si el contenido son solo letras
    cadena.isalnum()            # Valida si el contenido son solo caracteres alfanuméricos

    # División y Unión

    cadena.split("/")           # Divide un string en una lista usando un separador
                                # (Por defecto es espacio)
    cadena.join(["A", "B", "C"])      # Une elementos de una lista en un solo string que
                                # retorna usando la cadena como separador o unión.

    print(f"Cadena final: '{cadena}'")

def basic_sec_rangos():
    """range: Es una secuencia inmutable que genera números bajo demanda (lazy evaluation)."""

    r = range(0, 10, 2) # range(Inicio, Fin, Paso): 0, 2, 4, 6, 8

    r.count(4)          # Cuenta las veces que aparece el valor en el rango
                        # Debido a como funciona range, siempre mostrara 1 si está o 0 si no

    r.index(8)          # Indica la posición del valor dentro del rango. Si no esta lanza ValueError

    # Atributos de Range
    r.start
    r.stop
    r.step

    print(f"Rango final: {list(r)}")

def basic_col_diccionarios():
    """Diccionarios (dict): Mutables, almacenan pares clave:valor."""

    hp_personajes = {
        "elfo": 45,
        "barbaro": 30,
        "mago": 50,
    }
    hp_personajes_2 = {
        "ladron": 25,
        "elfo": 40,
    }

    # Métodos de Acceso y Consulta

    hp_personajes.get("", 0) # Devuelve el valor de la clave.
    # Si la clave no existe, devuelve default (o None si no lo especificas) en lugar de dar error

    hp_personajes.keys() # Devuelve una vista de todas las claves.
    hp_personajes.values() # Devuelve una vista de todos los valores.
    hp_personajes.items() # Devuelve una vista de parejas (clave, valor)

    # Métodos de Modificación e Inserción
    hp_personajes.update(hp_personajes_2) # Actualiza el diccionario con los pares clave/valor de
                    # otro diccionario. Si la clave ya existe, la sobreescribe; si no, la añade.

    hp_personajes.setdefault("hada", 2)  # Si la clave existe, devuelve su valor
                                            # Si no existe, inserta la clave con el valor default.

    hp_personajes.pop("key", "La clave no existe")
    # Elimina la clave y devuelve su valor. Si no existe, devuelve default.

    hp_personajes.popitem()
    # Elimina y devuelve el último par (clave, valor) insertado (útil para pilas LIFO).

    # Métodos de Copia
    backup = hp_personajes.copy() # Crea una copia superficial (independiente) del diccionario.

    hp_personajes.clear() # Vacía el diccionario por completo.

    print(f"Diccionario final: {backup}")

def basic_col_sets():
    """Sets (set): Mutables, no ordenados, no permiten duplicados."""

    mi_set = {1, 2, 3, 4, 5}
    set_sec = {0, 2, 4, 6, 8}

    # Métodos de Modificación (Mutación)
    mi_set.add(6) # Añade un elemento al set. Si ya existe, no hace nada.
    mi_set.remove(2) # Elimina el elemento. Si no existe, lanza un KeyError.
    mi_set.discard(10) # Igual que remove, pero no lanza error si el elemento no está.
    mi_set.pop() #  Elimina y devuelve un elemento arbitrario del set.
    mi_set.update([2, 7, 8]) # Añade varios elementos a la vez desde otra colección.
    #mi_set.clear() # Vacía el conjunto.

    # Métodos de Operaciones de Conjuntos
        # Devuelve un nuevo set con todos los elementos de ambos.
    mi_set.union(set_sec) # Puede recibir cualquier iterable
    mi_set | set_sec
        # Devuelve un nuevo set con los elementos que están en ambos.
    mi_set.intersection(set_sec) # Puede recibir cualquier iterable
    mi_set & set_sec
        # Devuelve elementos que están en el primero pero no en el segundo.
    mi_set.difference(set_sec) # Puede recibir cualquier iterable
    mi_set - set_sec
        # Devuelve elementos que están en uno u otro, pero no en ambos a la vez.
    mi_set.symmetric_difference(set_sec) # Puede recibir cualquier iterable
    mi_set ^ set_sec

    sub = {1, 2, 3}  # Los siguientes pueden recibir cualquier iterable
        # Si es subconjunto
    sub.issubset(mi_set) # Devuelve True si todos los elementos del set están dentro del otro.
        # Si es Superconjunto
    mi_set.issuperset(sub) # Devuelve True si el set contiene todos los elementos del otro.
        # Intersección vacía
    mi_set.isdisjoint({30, 40, 50}) # Retorna True si dos conjuntos no tienen elementos en común.

    mi_set.copy() # Devuelve una copia (aunque como es inmutable, técnicamente es el mismo objeto).

    print(f"Conjunto final: {list(mi_set)}")

def basic_col_frozenset():
    """frozenset: Es la versión inmutable de un set. Al ser inmutable, puede usarse como clave
    en un diccionario o set(a diferencia de un set normal).
    """

    mi_frozenset = frozenset({"A", "B", "C"})
    frozenset_sec = frozenset({"C", "D", "E"})

    # Métodos de Operaciones de Conjuntos
        # Devuelve un nuevo set con todos los elementos de ambos.
    mi_frozenset.union(frozenset_sec)
    mi_frozenset | frozenset_sec
        # Devuelve un nuevo set con los elementos que están en ambos.
    mi_frozenset.intersection(frozenset_sec)
    mi_frozenset & frozenset_sec
        # Devuelve elementos que están en el primero pero no en el segundo.
    mi_frozenset.difference(frozenset_sec)
    mi_frozenset - frozenset_sec
        # Devuelve elementos que están en uno u otro, pero no en ambos a la vez.
    mi_frozenset.symmetric_difference(frozenset_sec)
    mi_frozenset ^ frozenset_sec

    sub = {1, 2, 3}
        # Si es subconjunto
    sub.issubset(mi_frozenset) # Devuelve True si todos los elementos del set están dentro del otro.
        # Si es Superconjunto
    mi_frozenset.issuperset(sub) # Devuelve True si el set contiene todos los elementos del otro.
    mi_frozenset.isdisjoint({30, 40, 50})

    mi_frozenset.copy() # Retorna la misma dirección de memoria por ser inmutable

    print(f"Frozen Set Final: {list(mi_frozenset)}")

def basic_bin_bytes():
    """bytes: Secuencias inmutables de enteros (de 0 a 255) que sepresentan datos binarios puros."""

    # Los bytes se declaran anteponiendo una 'b' a las comillas
    b_secuencia = b"Hola Mundo Python"
    b"\x48\x6f\x6c\x61" # También puedes declararlos en hexadecimal

    # Métodos de búsqueda y análisis
    b_secuencia.count(b'o') # Cuenta cuántas veces aparece un byte o secuencia de bytes.
    b_secuencia.find(b'Mundo') # Devuelve el índice de primer aparición. Si no existe, devuelve -1.
    b_secuencia.index(b'Python') # Igual que find, pero lanza ValueError si no encuentra el valor.
    b_secuencia.startswith(b'Hola') # Devuelve True si la secuencia empieza con los bytes dados.
    b_secuencia.endswith(b'Python') # Devuelve True si la secuencia termina con los bytes dados.

    # Métodos de transformación (Devuelven nuevos objetos)
    # Nota: Son inmutables, por lo que b_secuencia no cambia
    b_secuencia.upper()
    b_secuencia.replace(b"Python", b"Mundo")
    b"   bytes con espacios   ".strip()

    # Métodos de conversión
        # Convertir a texto (decode)
    b_secuencia.decode("utf-8")
        # Convertir a Hexadecimal
    b_secuencia.hex() # '486f6c61204d756e646f20507974686f6e'
        # Convertir de Hexadecimal (método de clase)
    bytes.fromhex("486f6c61") # b'Hola'

    print(f"Bytes Final: {b_secuencia}")

def basic_bin_bytearray():
    """bytearray: Estructuras mutables para manejar datos binarios puros."""

    ba = bytearray(b"Datos Binarios")

    # Métodos de mutación
        #Añade un entero (0-255) al final.
    ba.append(33)           # Añade el byte 33 ('!') al final
        #Añade varios bytes a la vez desde otro iterable.
    ba.extend(b" extras")    # Extiende con nuevos bytes
        # Inserta un byte en una posición específica.
    ba.insert(0, 42)        # Inserta un '*' (42) al principio
    ba[0] = 74  # Cambia '*' por 'J'
    ba[2:5] = b"rro" # Cambia 'tos' por 'rro'
        # Invierte el orden de los bytes.
    #ba.reverse()            # Invierte todo el array
        # Elimina y devuelve el byte en el índice indicado (si no se especifica, elimina el último).
    ba.pop()                # Elimina la 's' del final.
        # Elimina la primera aparición del valor especificado.
    #ba.remove(255)
        # Remplaza la secuencia encontrada por la especificada.
    ba = ba.replace(b"D", b"a")
        # Vacía completamente el bytearray.
    # ba.clear()

    # Métodos compartidos(Busqueda/Transformación)
    # Al igual que los bytes, tienen los métodos de búsqueda
    ba.count(ord('a'))

    bytes(ba) # Puedes volver a bytes inmutables en cualquier momento

    print(f"bytearray Final: {ba}")

# Módulo collections

def advanced_col_deque():
    """deque: Cola de doble extremo, optimizada para añadir/quitar por ambos lados."""
    dq = deque([1, 2, 3])

    # Inserción
    dq.append(4)          # Añade al final
    dq.appendleft(0)      # Añade al principio

    # Eliminación
    dq.pop()              # Elimina y devuelve el del final
    dq.popleft()          # Elimina y devuelve el del principio

    # Extensión
    dq.extend([4, 5])         # Añade iterable al final
    dq.extendleft([-1, -2])   # Añade iterable al principio (invierte el orden del iterable)

    # Rotación y Otros
    dq.rotate(1)          # Rota elementos a la derecha (positivo) o izquierda (negativo) N pasos
    dq.remove(2)          # Elimina la primera ocurrencia del valor
    dq.count(3)           # Cuenta ocurrencias
    dq.reverse()          # Invierte en el sitio
    #dq.clear()            # Vacía la estructura

    print(f"Deque final: {dq}")

def advanced_col_namedtuple():
    """namedtuple: Tupla inmutable donde los campos tienen nombre (accesibles por punto)."""
    # Definición: nombre de la clase y cadena con nombres de campos
    Punto = namedtuple('Punto', ['x', 'y'])
    p = Punto(10, 20)

    # Acceso
    p.x                   # Acceso por nombre (más legible que p[0])
    p.y

    # Conversión y otros
    p._asdict()           # Retorna un OrderedDict con los valores
    p._replace(x=5)       # Retorna una nueva instancia con el campo cambiado
    
    print(f"NamedTuple: {p}")

def advanced_col_counter():
    """Counter: Subclase de dict para contar elementos hashables."""
    lista = ['rojo', 'azul', 'rojo', 'verde', 'azul', 'azul']
    c = Counter(lista)

    c.update(['verde', 'verde']) # Suma nuevas ocurrencias
    c.most_common(2)             # Devuelve los N elementos más comunes
    c.subtract(['rojo'])         # Resta ocurrencias

    # Operaciones matemáticas (se mantienen solo los conteos positivos)
    #pylint: disable=expression-not-assigned
    c + Counter(['azul'])        # Suma de conteos

    print(f"Counter final: {c}")

def advanced_col_defaultdict():
    """defaultdict: Diccionario que proporciona un valor por defecto si la clave no existe."""
    # Se inicializa con una factory function (list, int, set, etc.)
    dd = defaultdict(list)

    # Si la clave 'frutas' no existe, crea una lista vacía automáticamente y luego añade
    dd['frutas'].append('manzana')
    dd['frutas'].append('pera')

    # A diferencia del dict normal, no da KeyError
    print(dd['vegetales']) # Retorna [] (resultado de llamar a list())

    print(f"DefaultDict final: {dict(dd)}")

def _main():
    """Demo del programa. Ejecución principal"""
    _clear_console()
    print("-" * 20)
    print("Roadmap 04 - Estructuras de Datos")
    print("-" * 20)

    basic_sec_lista()
    basic_sec_tuplas()
    basic_sec_str()
    basic_sec_rangos()
    basic_col_diccionarios()
    basic_col_sets()
    basic_col_frozenset()
    basic_bin_bytes()
    basic_bin_bytearray()
    advanced_col_deque()
    advanced_col_namedtuple()
    advanced_col_counter()
    advanced_col_defaultdict()

    _enter_to_continue()
# =========================
# Demo del Programa
# =========================
if __name__ == "__main__":
    _main()
