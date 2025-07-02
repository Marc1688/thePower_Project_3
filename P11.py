# Pregunta 11:
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

try:
    edad = float(input("Por favor, ingresa tu edad: "))
    if edad < 0 or edad > 120:
        print("Error: La edad debe estar entre 0 y 120 años.")
    else:
        print(f"Tu edad es {int(edad)} años.")
except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido.")