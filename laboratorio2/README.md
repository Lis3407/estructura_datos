# Laboratorio 2: Árbol de Merkle

## Autor
Liseth Andrea Bedoya Cuervo

## Descripción

Este proyecto implementa un Árbol de Merkle utilizando Python y SHA-256.
El programa permite construir el árbol a partir de cinco bloques de datos,
obtener la Merkle Root y realizar verificaciones de inclusión válidas e
inválidas.

## Estructura del proyecto

```text
estructura_datos/laboratorio1
│
├── README.md 
├── Captura de pantalla.png
├── arbolMerkle.txt
└── arbolMerkle.py
```

### - **`README.md`**: 
Archivo actual.

### - **`Captura de pantalla.png`**: 
Contiene la captura de pantalla de las verificaciones solicitadas, 
incluyendo la verificación válida y la verificación con datos incorrectos.

### - **`arbolMerkle.txt`**:
Contiene el diagrama ASCII del Árbol de Merkle construido a partir de los cinco bloques.

### - **`arbolMerkle.py`**: 
Contiene el código fuente para la implementación del Árbol de Merkle, 
la construcción del árbol y las funciones de verificación.

El programa permite construir el árbol a partir de cinco bloques de datos,
obtener la Merkle Root, comprobar que una modificación en un bloque cambia
la raíz y realizar pruebas de inclusión.

**Funcionamiento**

El programa realiza las siguientes operaciones:

1. Crea 5 bloques de datos simulando transacciones.
2. Calcula el hash SHA-256 de cada bloque.
3. Construye el Árbol de Merkle combinando los hashes de dos en dos.
4. Duplica el último nodo cuando un nivel tiene un número impar de nodos.
5. Muestra la Merkle Root original.
6. Modifica el bloque 3 y comprueba que la Merkle Root cambia.
7. Genera una prueba de inclusión para el bloque 3.
8. Verifica que el bloque 3 pertenece al árbol.
9. Realiza una verificación utilizando un bloque incorrecto y comprueba que
   la prueba falla.

**Bloques utilizados**

Los cinco bloques utilizados en el experimento son:

- **Bloque 1:** Juan le paga $50 a Pedro
- **Bloque 2:** Maria compra un computador
- **Bloque 3:** Carlos deposita $100000
- **Bloque 4:** Ana compra un libro
- **Bloque 5:** Pablo compra 3 helados

**Prueba de inclusión**

Se genera una prueba de inclusión para el bloque 3.

La prueba permite reconstruir el camino desde el hash del bloque 3 hasta la
Merkle Root utilizando los hashes de sus hermanos.

Para el bloque 3, el proceso de verificación es:

```text
H3 + H4 → H34
H12 + H34 → H1234
H1234 + H5555 → MERKLE ROOT
```


