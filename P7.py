# Pregunta 7:
# Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map().

def tuplas_a_strings(lista_tuplas):
    # Usamos map() con una función lambda para convertir cada tupla en un string
    strings = list(map(lambda t: str(t), lista_tuplas))
    return strings

# Ejemplo de uso
tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_a_strings(tuplas)
print(resultado)