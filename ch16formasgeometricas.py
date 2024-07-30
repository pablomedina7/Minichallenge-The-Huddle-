import math

# Definición de la clase base FormaGeometrica
class FormaGeometrica:
    def calcular_area(self):
        pass  # Este método debe ser implementado en las clases derivadas
    
    def calcular_perimetro(self):
        pass  # Este método debe ser implementado en las clases derivadas

# Definición de la clase derivada Rectangulo
class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Definición de la clase derivada Circulo
class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Creación de objetos y cálculos
rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)

# Cálculos para el rectángulo
print("Rectángulo:")
print(f"Base: {rectangulo.base}, Altura: {rectangulo.altura}")
print(f"Área: {rectangulo.calcular_area()}")
print(f"Perímetro: {rectangulo.calcular_perimetro()}")

# Cálculos para el círculo
print("\nCírculo:")
print(f"Radio: {circulo.radio}")
print(f"Área: {circulo.calcular_area()}")
print(f"Perímetro: {circulo.calcular_perimetro()}")
