# Pregunta 35: 
# Crear la clase UsuarioBanco con operaciones de saldo y transferencias.

class UsuarioBanco:
    def __init__(self, nombre, saldo_inicial, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"No hay suficiente saldo para retirar {cantidad}. Saldo actual: {self.saldo}")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("El destinatario debe ser una instancia de UsuarioBanco.")
        if cantidad > self.saldo:
            raise ValueError(f"No hay suficiente saldo para transferir {cantidad}. Saldo actual: {self.saldo}")
        # Transferencia
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
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