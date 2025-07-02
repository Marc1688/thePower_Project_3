# Pregunta 10:
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

# Definir una excepción personalizada
class ListaVaciaError(Exception):
    pass

def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    promedio = sum(numeros) / len(numeros)
    return promedio

# Ejemplo de uso con manejo de errores
try:
    lista_numeros = []
    resultado = calcular_promedio(lista_numeros)
    print(f"El promedio es: {resultado}")
except ListaVaciaError as e:
    print(f"Error: {e}")