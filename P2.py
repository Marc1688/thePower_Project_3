# Pregunta 2:
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map().

# Ejemplo de lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicamos la función map() con una función lambda para doblar cada número
dobles = list(map(lambda x: x * 2, numeros))

print(dobles)