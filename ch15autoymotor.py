# Clase Motor
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        return f"Motor de tipo {self.tipo} con potencia de {self.potencia} caballos de fuerza."

# Clase Auto que contiene una instancia de Motor
class Auto:
    def __init__(self, marca, modelo, tipo_motor, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor, potencia_motor)

    def describir_auto(self):
        descripcion_motor = self.motor.describir()
        return f"Auto marca {self.marca}, modelo {self.modelo}, con {descripcion_motor}"

# Crear una instancia de Auto
mi_auto = Auto("Toyota", "Corolla", "Gasolina", 132)

# Describir el auto
descripcion = mi_auto.describir_auto()
print(descripcion)
