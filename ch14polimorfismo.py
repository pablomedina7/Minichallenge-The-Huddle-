# Clase base Animal
class Animal:
    def hacerSonido(self):
        print("El animal hace un sonido.")

# Clase derivada Perro que extiende Animal
class Perro(Animal):
    def hacerSonido(self):
        print("El perro ladra: ¡Guau!")

# Crear una instancia de Animal
animal = Animal()
animal.hacerSonido()

# Crear una instancia de Perro
perro = Perro()
perro.hacerSonido()
