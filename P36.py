# Pregunta 36: 
# Funciones para procesar un texto según diferentes opciones.

import re

def _tokenizar(texto):
    # Convierte a minúsculas, elimina puntuación y divide
    limpio = re.sub(r'[^\w\s]', '', texto.lower())
    return limpio.split()

def contar_palabras(texto):
    palabras = _tokenizar(texto)
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return conteo

def reemplazar_palabras(texto, orig, nuevo):
    # Para reemplazar coincidencias exactas, trabajamos sobre tokens
    tokens = _tokenizar(texto)
    return ' '.join(nuevo if t == orig.lower() else t for t in tokens)

def eliminar_palabra(texto, palabra):
    tokens = _tokenizar(texto)
    return ' '.join(t for t in tokens if t != palabra.lower())

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Reemplazar requiere: (palabra_original, palabra_nueva)")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Eliminar requiere: (palabra_eliminar,)")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida. Use 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso completo
texto_ejemplo = "Hola mundo. Este es un ejemplo de procesamiento de texto. Mundo, mundo!"
print("Contar palabras:", procesar_texto(texto_ejemplo, "contar"))
print("Reemplazar 'mundo' por 'universo':", procesar_texto(texto_ejemplo, "reemplazar", "mundo", "universo"))
print("Eliminar 'mundo':", procesar_texto(texto_ejemplo, "eliminar", "mundo"))
