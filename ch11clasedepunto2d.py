class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

# Crear una instancia de Punto2D
punto = Punto2D(3, 4)

# Imprimir las coordenadas del punto
punto.imprimir_coordenadas()
