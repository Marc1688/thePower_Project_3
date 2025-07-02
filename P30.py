# Pregunta 30:
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    # Convertir las palabras a minúsculas y ordenar sus letras
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplo de uso
palabra_a = "Escuchar"
palabra_b = "Chacurse"
resultado = son_anagramas(palabra_a, palabra_b)
print(f"Las palabras '{palabra_a}' y '{palabra_b}' son anagramas: {resultado}")