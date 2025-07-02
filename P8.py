# Pregunta 8:
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
# Muestra un mensaje indicando si la división fue exitosa o no.

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    resultado = num1 / num2
    print(f"La división es exitosa. Resultado: {resultado}")
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")