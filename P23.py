# Pregunta 23:
# Concatena una lista de palabras usando la función reduce().

from functools import reduce

def concatenar_palabras(palabras):
    # Usar reduce para concatenar todas las palabras en una sola cadena, separadas por espacio
    resultado = reduce(lambda acc, palabra: acc + ' ' + palabra if acc else palabra, palabras, "")
    return resultado

# Ejemplo de uso
lista_palabras = ["Hola", "cómo", "estás", "hoy"]
resultado = concatenar_palabras(lista_palabras)
print(resultado)