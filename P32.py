# Pregunta 32:
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelva el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

import unicodedata

def _normalizar(texto):
    # Elimina acentos y otros diacríticos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto.lower())
        if unicodedata.category(c) != 'Mn'
    )

def buscar_puesto(nombre_completo, empleados):
    nombre_norm = _normalizar(nombre_completo)
    for e in empleados:
        if _normalizar(e['nombre']) == nombre_norm:
            return f"{nombre_completo} trabaja como {e['puesto']}."
    return f"{nombre_completo} no trabaja aquí."

# Ejemplo de uso
empleados = [
    {'nombre': 'Carlos Pérez', 'puesto': 'Gerente'},
    {'nombre': 'Ana Gómez', 'puesto': 'Analista'},
    {'nombre': 'Luis Martínez', 'puesto': 'Desarrollador'}
]

print(buscar_puesto('Ana Gomez', empleados))
print(buscar_puesto('María Lopez', empleados))
