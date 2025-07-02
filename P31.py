# Pregunta 31:
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    try:
        # Solicitar al usuario ingresar una lista de nombres
        nombres_entrada = input("Ingrese una lista de nombres separados por comas: ")
        lista_nombres = [nombre.strip() for nombre in nombres_entrada.split(',')]
        
        # Solicitar el nombre a buscar
        nombre_a_buscar = input("Ingrese el nombre a buscar: ").strip()
        
        # Buscar el nombre en la lista
        if nombre_a_buscar in lista_nombres:
            print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_a_buscar}' no está en la lista.")
    except ValueError as e:
        print(e)

# Ejemplo de uso
buscar_nombre()