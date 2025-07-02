# Pregunta 29:
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    else:
        return '#' * (len(cadena) - 4) + cadena[-4:]

# Ejemplo de uso
variable = 123456789
resultado = enmascarar_variable(variable)
print(f"Variable enmascarada: {resultado}")