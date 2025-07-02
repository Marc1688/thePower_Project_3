# Pregunta 28:
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def buscar_primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  

# Ejemplo de uso
lista_ejemplo = [3, 5, 1, 2, 4, 5, 6]
resultado = buscar_primer_duplicado(lista_ejemplo)
print(f"El primer elemento duplicado es: {resultado}")