"""
    Generar Matriz de 100,000×100,000 en disco duro

    Crea una matriz de 100,000 filas por 100,000 columnas,
    compuesta únicamente por valores 0. La matriz se almacena
    directamente en disco duro.

    La matriz se representa mediante caracteres "0" en formato
    ASCII, donde cada carácter ocupa 1 Byte. Cada fila termina
    con el carácter "|" como separador, permitiendo identificar
    dónde termina una fila al momento de leer el archivo.

    Para mejorar la eficiencia de escritura, las filas se agrupan
    en bloques de 100 filas. Estos bloques se escriben directamente
    en el archivo, evitando realizar una operación de escritura
    individual para cada fila.

    Archivo resultante:
    - Archivo: matriz.txt
    - Cada fila contiene 100,000 caracteres "0"
    - Cada fila termina con el carácter "|"
    - Total: 100,000 filas
    - Total de columnas: 100,000
    - Filas escritas por bloque: 100
    - Bloques completos: 1,000
    - Filas restantes: 0
"""

# Cantidad de filas que tendrá la matriz.
FILAS = 100_000

# Cantidad de columnas que tendrá cada fila.
COLUMNAS = 100_000

# Nombre del archivo donde se almacenará la matriz.
ARCHIVO = "matriz.txt"

'''
Se crea una fila formada por 100.000 ceros.

b"0" representa el carácter '0' en formato de bytes.
Al multiplicarlo por COLUMNAS, se generan 100.000 ceros.

Al final se agrega el carácter "|" como separador de filas. 
Lo que permite identificar dónde termina una fila al leer el archivo.
'''
fila = b"0" * COLUMNAS + b"|"

'''
Cantidad de filas que se escribirán simultáneamente en el archivo.

En lugar de escribir las 100.000 filas una por una, se agrupan
de 100 en 100 para reducir la cantidad de operaciones de escritura.
'''
FILAS_POR_BLOQUE = 100

'''
Se crea un bloque compuesto por 100 filas.

Como "fila" ya contiene una fila completa de la matriz,
multiplicarla por 100 genera un bloque de 100 filas.
'''
bloque = fila * FILAS_POR_BLOQUE

'''
Se abre el archivo en modo escritura binaria ("wb").

"w"  -> permite escribir en el archivo.
"b"  -> indica que se trabajará con bytes.

Si el archivo ya existe, su contenido será reemplazado.
'''
with open(ARCHIVO, "wb") as archivo:

    '''
    Calcula cuántos bloques completos de 100 filas
    pueden formarse con las 100.000 filas.
    
    100.000 // 100 = 1.000 bloques completos.
    '''
    bloques_completos = FILAS // FILAS_POR_BLOQUE

    '''
    Calcula cuántas filas quedan después de formar
    todos los bloques completos.
    
    100.000 % 100 = 0 filas restantes.
    '''
    filas_restantes = FILAS % FILAS_POR_BLOQUE

    '''
    Se escribe cada bloque de 100 filas en el archivo.
    
    Como existen 1.000 bloques completos, este ciclo
    realizará 1.000 operaciones de escritura.
    '''
    for _ in range(bloques_completos):
        archivo.write(bloque)


    # Si después de formar los bloques completos quedaron
    # algunas filas sin escribir, se escriben aquí.
    if filas_restantes > 0:
        archivo.write(fila * filas_restantes)

# Se muestra un mensaje indicando que el archivo fue creado.
print("Matriz creada correctamente.")