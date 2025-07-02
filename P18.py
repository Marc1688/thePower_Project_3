# Pregunta 18:
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificación": 95},
    {"nombre": "Luis", "edad": 22, "calificación": 88},
    {"nombre": "Carlos", "edad": 19, "calificación": 92},
    {"nombre": "María", "edad": 21, "calificación": 85},
    {"nombre": "Sofía", "edad": 23, "calificación": 97}
]

# Usar filter() para extraer estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda e: e["calificación"] >= 90, estudiantes))

# Imprimir los estudiantes destacados
for estudiante in estudiantes_destacados:
    print(estudiante)