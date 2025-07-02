# Pregunta 34: 
# Crear la clase Arbol con atributos y métodos para manipular su estructura.

class Arbol:
    def __init__(self):
        self.tronco = 1  # Longitud inicial del tronco
        self.ramas = []  # Lista vacía de ramas

    def crecer_tronco(self):
        """Incrementa la longitud del tronco en 1."""
        self.tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Incrementa en 1 la longitud de todas las ramas existentes."""
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama en la posición especificada (0-based)."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida para quitar rama.")

    def info_arbol(self):
        """Devuelve información del árbol: longitud del tronco, número y longitudes de las ramas."""
        info = {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
        return info

# Caso de uso:
# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama en la posición 2 (tercera)
arbol.quitar_rama(2)

# 7. Obtener información
info = arbol.info_arbol()
print(info)