# Pregunta 3:
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def palabras_con_objetivo(lista_palabras, palabra_objetivo):
    # Crear una nueva lista con las palabras que contienen la palabra objetivo
    resultado = [palabra for palabra in lista_palabras if palabra_objetivo in palabra]
    return resultado

# Ejemplo de uso
lista = ["manzana", "naranja", "plátano", "sandía", "manos"]
objetivo = "an"
resultado = palabras_con_objetivo(lista, objetivo)
print(resultado)