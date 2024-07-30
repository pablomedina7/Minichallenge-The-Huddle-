# Clase base Figura
class Figura:
    def imprimir(self):
        print("Esta es una figura genérica.")

# Clase derivada Círculo que extiende Figura
class Círculo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Este es un círculo con radio {self.radio}.")

# Crear una instancia de Figura
figura = Figura()
figura.imprimir()

# Crear una instancia de Círculo
circulo = Círculo(5)
circulo.imprimir()
