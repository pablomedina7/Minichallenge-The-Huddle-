class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def __str__(self):
        return str(self.stack)

# Crear una instancia de Stack
stack = Stack()

# Insertar 5 elementos en la pila
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

# Mostrar la pila después de insertar los elementos
print("Pila después de insertar 5 elementos:")
print(stack)

# Eliminar elementos de la pila
print("\nElementos eliminados de la pila en orden:")
while not stack.is_empty():
    print(stack.pop())
