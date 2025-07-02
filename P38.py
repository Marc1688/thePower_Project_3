# Pregunta 38: 
# Programa que determina la calificación en texto basada en la calificación numérica.

def determinar_calificacion(nota):
    """Devuelve la calificación en texto según la nota numérica."""
    if not (0 <= nota <= 100):
        raise ValueError("La nota debe estar entre 0 y 100.")
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"

try:
    nota_usuario = float(input("Ingresa la calificación numérica (0-100): "))
    calificacion_texto = determinar_calificacion(nota_usuario)
    print(f"La calificación en texto es: {calificacion_texto}")
except ValueError as e:
    print(f"Error: {e}")