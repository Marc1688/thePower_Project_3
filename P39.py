# Pregunta 39: 
# Función que calcula el área de una figura según su tipo y datos.

def calcular_area(figura, datos):
    if figura == "rectangulo":
        # Datos: (base, altura)
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        # Datos: (radio,)
        radio, = datos
        from math import pi
        return pi * radio ** 2
    elif figura == "triangulo":
        # Datos: (base, altura)
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no reconocida. Use 'rectangulo', 'circulo' o 'triangulo'.")

# Ejemplo de uso:
area_rectangulo = calcular_area("rectangulo", (5, 10))
area_circulo = calcular_area("circulo", (7,))
area_triangulo = calcular_area("triangulo", (6, 8))

print(f"Área de rectángulo: {area_rectangulo}")
print(f"Área de círculo: {area_circulo}")
print(f"Área de triángulo: {area_triangulo}")