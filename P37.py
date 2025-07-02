# Pregunta 37: 
# Programa que indica si es de noche, día o tarde según la hora proporcionada.

def determinar_tiempo(hora):
    """Devuelve 'noche', 'día' o 'tarde' según la hora en 24 horas."""
    if not (0 <= hora <= 23):
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 12:
        return "Es día."
    elif 12 <= hora < 20:
        return "Es tarde."
    else:
        return "Es noche."

try:
    hora_usuario = int(input("Ingresa la hora en formato 24 horas (0-23): "))
    resultado = determinar_tiempo(hora_usuario)
    print(resultado)
except ValueError as e:
    print(f"Error: {e}")