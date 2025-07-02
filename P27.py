# Pregunta 27:
# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)

# Ejemplo de uso
lista_numeros = [10, 20, 30, 40]
resultado = calcular_promedio(lista_numeros)
print(f"El promedio de la lista es: {resultado}")