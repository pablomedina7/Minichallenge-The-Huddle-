class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def consultar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")
        return self.saldo

# Crear una instancia de CuentaBancaria con un saldo inicial de 100
cuenta = CuentaBancaria(1000000)

# Consultar el saldo inicial
cuenta.consultar_saldo()

# Depositar 50 en la cuenta
cuenta.depositar(50000)

# Consultar el saldo después del depósito
cuenta.consultar_saldo()
