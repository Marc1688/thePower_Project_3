# Pregunta 24:
# Calcula la diferencia total en los valores de una lista usando la función reduce().

from functools import reduce

def diferencia_total(numeros):
    # Usar reduce para restar todos los elementos
    diferencia = reduce(lambda acc, x: acc - x, numeros)
    return diferencia

# Ejemplo de uso
lista_numeros = [100, 20, 30]
resultado = diferencia_total(lista_numeros)
print(f"La diferencia total en {lista_numeros} es {resultado}")