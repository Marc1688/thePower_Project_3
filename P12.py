# Pregunta 12:
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
# Usa la función map().

def longitudes_palabras(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    # Usar map() para obtener la longitud de cada palabra
    longitudes = list(map(len, palabras))
    return longitudes

# Ejemplo de uso
frase = "Hola, ¿cómo estás hoy?"
resultado = longitudes_palabras(frase)
print(resultado)