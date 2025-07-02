# Pregunta 17:
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5,7,2] corresponde al número 572.
# Usa la función reduce().

from functools import reduce

def lista_a_numero(digitos):
    # Usar reduce para construir el número
    numero = reduce(lambda acc, d: acc * 10 + d, digitos, 0)
    return numero

# Ejemplo de uso
digitos = [5, 7, 2]
resultado = lista_a_numero(digitos)
print(resultado)