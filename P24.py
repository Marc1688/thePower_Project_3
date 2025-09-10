# Pregunta 24:
# Calcula la diferencia total en los valores de una lista usando la función reduce().

from functools import reduce

def diferencia_total(numeros):
    if not numeros:
        return 0  # O lanzar excepción si prefieres
    # Iniciamos el acumulador en el primer elemento, o bien en 0:
    return reduce(lambda acc, x: acc - x, numeros, 0)

# Ejemplo de uso
lista_numeros = [100, 20, 30]
resultado = diferencia_total(lista_numeros)
print(f"La diferencia total en {lista_numeros} es {resultado}")
