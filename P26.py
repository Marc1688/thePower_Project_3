# Pregunta 26:
# Crea una función lambda que calcule el resto de la división entre dos números dados.

# Función lambda para calcular el resto
calcular_resto = lambda x, y: x % y

# Ejemplo de uso
num1 = 17
num2 = 5
resultado = calcular_resto(num1, num2)
print(f"El resto de {num1} dividido entre {num2} es {resultado}")