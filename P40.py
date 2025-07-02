# Pregunta 40: 
# Programa que calcula el monto final de una compra con descuento en una tienda en línea.

# Paso 1: Solicitar precio original
precio_original = float(input("Ingresa el precio original del artículo: € "))

# Paso 2: Preguntar si tiene cupón de descuento
respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

descuento = 0  # Valor por defecto del descuento

# Paso 3 y 4: Validar respuesta y aplicar descuento si procede
if respuesta == "sí":
    valor_cupon = float(input("Ingresa el valor del cupón de descuento en €: "))
    if valor_cupon > 0:
        descuento = valor_cupon
    else:
        print("Valor del cupón inválido. No se aplicará descuento.")
elif respuesta == "no":
    print("No se aplicará ningún descuento.")
else:
    print("Respuesta no válida. Asumiendo que no hay descuento.")

# Paso 5: Calcular precio final
precio_final = precio_original - descuento
# Asegurarnos de que el precio final no sea negativo
precio_final = max(precio_final, 0)

# Paso 6: Mostrar resultado
print(f"El precio final de la compra es: € {precio_final:.2f}")