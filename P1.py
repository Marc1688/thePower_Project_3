# Pregunta 1:
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

def calcular_frecuencias(cadena):
    # Inicializar un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        if caracter != ' ':
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    
    return frecuencias

# Ejemplo de uso
cadena = "hola mundo"
resultado = calcular_frecuencias(cadena)
print(resultado)