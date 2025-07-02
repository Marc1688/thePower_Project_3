# Pregunta 15:
# Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de ejemplo
numeros = [1, 4, 7, 10]

sumar_tres = lambda x: x + 3

# Aplicar la lambda a cada elemento usando map()
resultado = list(map(sumar_tres, numeros))
print(resultado)