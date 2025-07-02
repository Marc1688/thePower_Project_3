# Pregunta 6:
# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")