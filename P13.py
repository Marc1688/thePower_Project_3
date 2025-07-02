# Pregunta 13:
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas. Usa la función map().

def letras_mayus_minus(conjunto):
    # Convertir el conjunto a una lista para poder mapear
    caracteres = list(conjunto)
    # Usar map() con una lambda que devuelve una tupla (mayúscula, minúscula) para cada carácter
    resultado = list(map(lambda c: (c.upper(), c.lower()), caracteres))
    return resultado

# Ejemplo de uso
conjunto_chars = {'a', 'b', 'c'}
resultado = letras_mayus_minus(conjunto_chars)
print(resultado)