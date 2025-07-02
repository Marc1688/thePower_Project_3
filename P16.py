# Pregunta 16:
# Escribe una función que tome una cadena de texto y un número entero n como parámetrosy devuelva una lista de todas las palabras que sean más largas que n.
# Usa la función filter().

def palabras_mas_largas_que_n(cadena, n):
    palabras = cadena.split()
    # Usar filter() con una lambda para filtrar las palabras que tengan longitud mayor que n
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))
    return resultado

# Ejemplo de uso
texto = "Esto es una prueba para filtrar palabras largas"
n = 4
resultado = palabras_mas_largas_que_n(texto, n)
print(resultado)