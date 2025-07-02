# Pregunta 4:
# Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map().

def diferencias_listas(lista1, lista2):
    # Usamos map() con una función lambda para restar los elementos correspondientes de las dos listas
    diferencias = list(map(lambda x, y: x - y, lista1, lista2))
    return diferencias

# Ejemplo de uso
lista_a = [10, 20, 30]
lista_b = [5, 15, 25]
resultado = diferencias_listas(lista_a, lista_b)
print(resultado)