import hashlib


# Representa un nodo del árbol y guarda su hash y sus hijos.
class Nodo:
    def __init__(self, hash, hijo_izquierdo=None, hijo_derecho=None):
        self.hash = hash
        self.hijo_izquierdo = hijo_izquierdo
        self.hijo_derecho = hijo_derecho


# Calcula el hash SHA-256 de una transacción.
def calcular_hash(transaccion):
    datos = str(transaccion).encode("utf-8")

    return hashlib.sha256(datos).hexdigest()


# Combina dos hashes para crear el hash del nodo padre.
def combinar_hashes(hash1, hash2):
    datos = (hash1 + hash2).encode("utf-8")

    return hashlib.sha256(datos).hexdigest()


# Construye el árbol de Merkle a partir de las transacciones.
def construir_arbol(transacciones):

    # Crear los nodos hoja.
    nodos = []

    for transaccion in transacciones:
        hash_transaccion = calcular_hash(transaccion)
        nodo = Nodo(hash_transaccion)
        nodos.append(nodo)

    # Construir los niveles superiores.
    while len(nodos) > 1:

        nuevo_nivel = []

        # Tomar los nodos de dos en dos.
        for i in range(0, len(nodos), 2):

            hijo_izquierdo = nodos[i]

            # Si falta un segundo nodo, se duplica el último.
            if i + 1 < len(nodos):
                hijo_derecho = nodos[i + 1]
            else:
                hijo_derecho = nodos[i]

            # Crear el hash del nodo padre.
            hash_padre = combinar_hashes(
                hijo_izquierdo.hash,
                hijo_derecho.hash
            )

            # Crear el padre con sus dos hijos.
            padre = Nodo(
                hash_padre,
                hijo_izquierdo,
                hijo_derecho
            )

            nuevo_nivel.append(padre)

        nodos = nuevo_nivel

    # El último nodo es la raíz del árbol.
    return nodos[0]


# Genera la prueba para comprobar que un bloque pertenece al árbol.
def generar_prueba(nodo, hash_buscado, prueba=None):

    if prueba is None:
        prueba = []

    # Si encontramos el bloque, terminamos la búsqueda.
    if nodo.hash == hash_buscado:
        return prueba

    # Buscar en el hijo izquierdo.
    if nodo.hijo_izquierdo is not None:

        resultado = generar_prueba(
            nodo.hijo_izquierdo,
            hash_buscado,
            prueba.copy()
        )

        if resultado is not None:

            # Guardar el hash del hermano derecho.
            if nodo.hijo_derecho is not None:
                resultado.append(
                    ("derecha", nodo.hijo_derecho.hash)
                )

            return resultado

    # Buscar en el hijo derecho.
    if nodo.hijo_derecho is not None:

        resultado = generar_prueba(
            nodo.hijo_derecho,
            hash_buscado,
            prueba.copy()
        )

        if resultado is not None:

            # Guardar el hash del hermano izquierdo.
            if nodo.hijo_izquierdo is not None:
                resultado.append(
                    ("izquierda", nodo.hijo_izquierdo.hash)
                )

            return resultado

    return None


# Verifica si la prueba permite llegar a la raíz esperada.
def verificar_prueba(transaccion, prueba, raiz_esperada):

    # Calcular el hash de la transacción.
    hash_actual = calcular_hash(transaccion)

    # Combinarlo con los hashes de los hermanos.
    for direccion, hash_hermano in prueba:

        if direccion == "derecha":
            hash_actual = combinar_hashes(
                hash_actual,
                hash_hermano
            )

        elif direccion == "izquierda":
            hash_actual = combinar_hashes(
                hash_hermano,
                hash_actual
            )

    # Comprobar si coincide con la raíz.
    return hash_actual == raiz_esperada

# -------------------------
# EXPERIMENTO
# -------------------------

# Crear 5 bloques de datos

bloque1 = "Juan le paga $50 a Pedro"
bloque2 = "Maria compra un computador"
bloque3 = "Carlos deposita $100000"
bloque4 = "Ana compra un libro"
bloque5 = "Pablo compra 3 helados"

transacciones = [
    bloque1,
    bloque2,
    bloque3,
    bloque4,
    bloque5
]


# Construir el árbol y mostrar la raíz

raiz_original = construir_arbol(transacciones)

print("\nMerkle Root original:")
print(raiz_original.hash)

# Modificar un bloque y demostrar que la raíz cambia

transacciones_modificadas = transacciones.copy()
transacciones_modificadas[2] = "Carlos deposita $200000"

raiz_modificada = construir_arbol(transacciones_modificadas)

print("\nMerkle Root modificada:")
print(raiz_modificada.hash)

if raiz_original.hash != raiz_modificada.hash:
    print("\nLa raíz cambió correctamente.")
else:
    print("\nLa raíz no cambió.")

# Generar una prueba de inclusión para el bloque 3 y verificar que es válida.

hash_bloque3 = calcular_hash(bloque3)

prueba = generar_prueba(
    raiz_original,
    hash_bloque3
)

print("\nPrueba de inclusión del bloque 3:")

for direccion, hash_hermano in prueba:
    print(f"Hermano a la {direccion}: {hash_hermano}")

resultado = verificar_prueba(
    bloque3,
    prueba,
    raiz_original.hash
)

print("\n¿La prueba de inclusión es válida?")

if resultado:
    print("Sí, el bloque 3 pertenece al árbol.")
else:
    print("No, el bloque 3 no pertenece al árbol.")

# Intentar verificar con un dato incorrecto

bloque3_incorrecto = "Carlos deposita $999999"

resultado_incorrecto = verificar_prueba(
    bloque3_incorrecto,
    prueba,
    raiz_original.hash
)

print("\nVerificación con un dato incorrecto:")

if resultado_incorrecto:
    print("La prueba es válida.")
else:
    print("La prueba no es válida.")

