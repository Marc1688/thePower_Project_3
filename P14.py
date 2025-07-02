# Pregunta 14:
# Crea una función que retorne las palabras de una lista de palabras que comiencen con una letra en específico.
# Usa la función filter().

def palabras_comienzan_con(letra, lista_palabras):
    # Convertir la letra a minúscula para hacer comparación insensible a mayúsculas/minúsculas
    letra = letra.lower()
    # Usar filter() con una lambda que verifica si la palabra comienza con la letra
    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))
    return resultado

# Ejemplo de uso
lista = ["Manzana", "mano", "Naranja", "Mango", "mundo"]
letra = "m"
resultado = palabras_comienzan_con(letra, lista)
print(resultado)