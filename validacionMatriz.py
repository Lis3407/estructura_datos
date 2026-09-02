"""
    Verificar Matriz de 100,000×100,000 almacenada en disco duro

    Lee el archivo "matriz.txt" y verifica que la matriz almacenada
    tenga las dimensiones esperadas: 100,000 filas por 100,000 columnas.

    El archivo utiliza el carácter "|" como separador de filas.
    Cada aparición de "|" representa el final de una fila, por lo
    que este carácter permite determinar la cantidad total de filas
    almacenadas en el archivo.

    Para verificar la cantidad de filas, el archivo se lee en bloques
    de 1 MB. Esto permite recorrer un archivo de gran tamaño sin cargar
    los aproximadamente 10 GB de información completos en la memoria RAM.

    Para verificar la cantidad de columnas, se lee únicamente la
    primera fila hasta encontrar el primer carácter "|". La cantidad
    de caracteres "0" encontrados antes del separador corresponde
    al número de columnas de esa fila.

    Finalmente, se muestra si la matriz tiene las dimensiones
    esperadas y se imprimen los elementos de la primera fila.

    Archivo utilizado:
    - Archivo: matriz.txt
    - Filas esperadas: 100,000
    - Columnas esperadas: 100,000
    - Separador de filas: "|"
    - Tamaño de lectura para verificar filas: 1 MB
"""


# Nombre del archivo que contiene la matriz almacenada en disco.
ARCHIVO = "matriz.txt"

# Dimensiones que debe tener la matriz para considerarse válida.
FILAS_ESPERADAS = 100_000
COLUMNAS_ESPERADAS = 100_000

#Contador de filas encontradas en el archivo.
filas = 0


'''
Variable que indica si la matriz cumple con las dimensiones
esperadas.

Inicialmente se considera que la matriz es válida.
Si alguna de las verificaciones falla, cambia a False.
'''
matriz_valida = True


'''
Se abre el archivo en modo lectura binaria ("rb").

"r" -> permite leer el archivo.
"b" -> indica que la información se manejará como bytes.

El archivo se lee por bloques para evitar cargar los
aproximadamente 10 GB completos en la memoria RAM.
'''
with open(ARCHIVO, "rb") as archivo:

    # Se continúa leyendo el archivo hasta llegar al final.
    while True:

        '''
        Lee un bloque de 1 MB del archivo.

        1024 * 1024 = 1,048,576 bytes = 1 MB.
        '''
        bloque = archivo.read(1024 * 1024)

        '''
        Si no quedan datos por leer, read() devuelve b"".
        En ese caso se termina el ciclo.
        '''
        if not bloque:
            break

        '''
        Cuenta cuántos separadores "|" existen en el bloque.

        Cada "|" representa el final de una fila.
        '''
        filas_en_bloque = bloque.count(b"|")

        '''
        Se acumula la cantidad de filas encontradas
        en el bloque actual.
        '''
        filas += filas_en_bloque


'''
Se compara la cantidad de filas encontradas con la cantidad
de filas esperadas.

Si son diferentes, la matriz no tiene las dimensiones
esperadas.
'''
if filas != FILAS_ESPERADAS:

    matriz_valida = False

    print(f"Error: se encontraron {filas} filas.")

else:

    print(f"Filas correctas: tiene {filas}")


'''
Para comprobar la cantidad de columnas no es necesario
recorrer nuevamente todo el archivo.

Como cada fila termina con "|", se puede leer la primera
fila hasta encontrar el primer separador.

La cantidad de caracteres "0" antes del "|" corresponde
a la cantidad de columnas de la fila.
'''
with open(ARCHIVO, "rb") as archivo:

    # Almacenará los caracteres de la primera fila.
    primera_fila = bytearray()

    '''
    Se lee el archivo carácter por carácter hasta encontrar
    el primer "|", que indica el final de la primera fila.
    '''
    while True:

        # Lee un carácter en formato de bytes.
        caracter = archivo.read(1)

        # Si encuentra "|", significa que terminó la primera fila.
        if caracter == b"|":
            break

        # Agrega el carácter leído a la primera fila.
        primera_fila.extend(caracter)


'''
La cantidad de elementos almacenados en primera_fila
corresponde a la cantidad de columnas.
'''
columnas = len(primera_fila)


'''
Se compara la cantidad de columnas encontradas en la primera
fila con la cantidad de columnas esperadas.
'''
if columnas != COLUMNAS_ESPERADAS:

    matriz_valida = False

    print(f"Error: la primera fila tiene {columnas} columnas.")

else:

    print(f"Columnas correctas: tiene {columnas}")

'''
Si las filas y las columnas coinciden con las dimensiones
esperadas, la matriz se considera válida.
'''
if matriz_valida:

    print("\nLa matriz tiene las dimensiones correctas:")
    print(f"{filas} filas x {columnas} columnas")

else:

    print("\nLa matriz no tiene las dimensiones esperadas.")


print("\nPrimera fila:")

'''
La primera fila contiene 100,000 caracteres "0".

Se muestran los elementos de la primera fila.
El método decode() convierte los bytes a texto para
poder mostrarlos correctamente en la consola.
'''
print(primera_fila.decode())
