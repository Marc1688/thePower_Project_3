# Pregunta 36: 
# Funciones para procesar un texto según diferentes opciones.

def contar_palabras(texto):
    """Cuenta la cantidad de veces que aparece cada palabra en el texto."""
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza todas las ocurrencias de palabra_original por palabra_nueva en el texto."""
    palabras = texto.split()
    palabras_reemplazadas = [palabra_nueva if p == palabra_original else p for p in palabras]
    return ' '.join(palabras_reemplazadas)

def eliminar_palabra(texto, palabra_eliminar):
    """Elimina todas las ocurrencias de palabra_eliminar del texto."""
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """Procesa el texto según la opción especificada."""
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Reemplazar requiere dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Eliminar requiere un argumento: palabra_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción inválida. Use 'contar', 'reemplazar' o 'eliminar'.")

# Caso de uso completo
texto_ejemplo = "Hola mundo. Este es un ejemplo de procesamiento de texto. Mundo, mundo!"
print("Contar palabras:", procesar_texto(texto_ejemplo, "contar"))
print("Reemplazar 'mundo' por 'universo':", procesar_texto(texto_ejemplo, "reemplazar", "mundo", "universo"))
print("Eliminar 'mundo':", procesar_texto(texto_ejemplo, "eliminar", "mundo"))