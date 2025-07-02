# Pregunta 32:
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelva el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, empleados):
    # empleados es una lista de diccionarios con 'nombre' y 'puesto'
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre_completo.lower():
            return f"{nombre_completo} trabaja como {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."

# Ejemplo de uso
empleados = [
    {'nombre': 'Carlos Pérez', 'puesto': 'Gerente'},
    {'nombre': 'Ana Gómez', 'puesto': 'Analista'},
    {'nombre': 'Luis Martínez', 'puesto': 'Desarrollador'}
]

print(buscar_puesto('Ana Gomez', empleados))
print(buscar_puesto('María Lopez', empleados))