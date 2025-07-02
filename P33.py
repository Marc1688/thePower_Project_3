# Pregunta 33:
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

# Listas de ejemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Función lambda usando zip y map para sumar elementos correspondientes
sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# Resultado
resultado = sumar_listas(lista1, lista2)
print(resultado)