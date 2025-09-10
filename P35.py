# Pregunta 35: 
# Crear la clase UsuarioBanco con operaciones de saldo y transferencias.

class UsuarioBanco:
    def __init__(self, nombre, saldo_inicial, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Si no tiene cuenta corriente, no permitir saldo negativo
        disponible = self.saldo if not self.tiene_cuenta_corriente else self.saldo + 0  # ajustar límite si hay descubierto
        if cantidad > disponible:
            raise ValueError(f"No hay saldo suficiente. Disponible: {disponible}")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("Destino debe ser UsuarioBanco.")
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad a agregar debe ser positiva.")
        self.saldo += cantidad

# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo 100, "Bob" con saldo 50, ambos con cuenta corriente
alice = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades a "Bob"
bob.agregar_dinero(20)

# 3. Transferir 80 unidades desde "Bob" a "Alicia"
try:
    bob.transferir_dinero(alice, 80)
except Exception as e:
    print(e)

# 4. Retirar 50 unidades de saldo a "Alicia"
try:
    alice.retirar_dinero(50)
except Exception as e:
    print(e)

# Mostrar saldos finales
print(f"{alice.nombre} saldo: {alice.saldo}")
print(f"{bob.nombre} saldo: {bob.saldo}")
