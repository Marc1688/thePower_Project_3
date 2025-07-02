# Pregunta 19:
# Crea una función lambda que filtre los números impares de una lista dada.

# Lista de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función lambda para filtrar impares
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Aplicar la función lambda
impares = filtrar_impares(numeros)
print(impares)