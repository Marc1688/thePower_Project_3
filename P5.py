# Pregunta 5:
# Escribe una función que tome una lista de números y un valor opcional nota_aprobado (por defecto 5).
# La función debe calcular la media de los números y determinar si la media es mayor o igual que nota_aprobado.
# Devuelve una tupla con la media y el estado ("aprobado" o "suspenso").

def evaluar_media(numeros, nota_aprobado=5):
    # Calcular la media de la lista
    media = sum(numeros) / len(numeros) if numeros else 0
    
    # Determinar el estado según la media
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    # Devolver una tupla con la media y el estado
    return (media, estado)

# Ejemplo de uso
lista_numeros = [4, 6, 7, 5]
resultado = evaluar_media(lista_numeros)  # nota_aprobado por defecto 5
print(resultado)