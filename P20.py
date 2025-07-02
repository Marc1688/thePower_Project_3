# Pregunta 20:
# Para una lista con elementos tipo integer y string, obtén una nueva lista solo con los valores int.
# Usa la función filter().

# Lista de ejemplo
lista_mixta = [1, "hola", 2, "mundo", 3, "python", 4]

# Usar filter() con una lambda que compruebe el tipo
solo_enteros = list(filter(lambda x: isinstance(x, int), lista_mixta))

# Mostrar resultado
print(solo_enteros)