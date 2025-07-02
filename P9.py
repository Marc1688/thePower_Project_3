# Pregunta 9:
# Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usa la función filter().

def filtrar_mascotas_prohibidas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Uso de filter() para excluir mascotas prohibidas
    mascotas_autorizadas = list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))
    return mascotas_autorizadas

# Ejemplo de uso
lista = ["Perro", "Gato", "Mapache", "Loro", "Oso", "Hámster"]
resultado = filtrar_mascotas_prohibidas(lista)
print(resultado)