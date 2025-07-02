# Pregunta 22:
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.
# Usa la función reduce().

from functools import reduce

def producto_lista(numeros):
    # Usar reduce para multiplicar todos los elementos
    producto = reduce(lambda acc, x: acc * x, numeros, 1)
    return producto

# Ejemplo de uso
lista_numeros = [2, 3, 4, 5]
resultado = producto_lista(lista_numeros)
print(f"El producto total de {lista_numeros} es {resultado}")