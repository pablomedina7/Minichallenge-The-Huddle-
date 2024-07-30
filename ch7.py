#Pilas y colas: Piloto de eventos (Priority Queue):
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, element, priority):
        new_item = (priority, element)
        if self.is_empty():
            self.queue.append(new_item)
        else:
            for i in range(len(self.queue)):
                if self.queue[i][0] < priority:
                    self.queue.insert(i, new_item)
                    break
            else:
                self.queue.append(new_item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]
        else:
            raise IndexError("dequeue from an empty priority queue")

    def __str__(self):
        return str([item[1] for item in self.queue])


# Crear una instancia de PriorityQueue
pq = PriorityQueue()

# Insertar 5 elementos con diferentes prioridades
pq.enqueue("Evento 1", 1)
pq.enqueue("Evento 2", 3)
pq.enqueue("Evento 3", 2)
pq.enqueue("Evento 4", 5)
pq.enqueue("Evento 5", 4)

# Mostrar la cola de prioridad después de insertar los elementos
print("Cola de prioridad después de insertar 5 elementos:")
print(pq)

# Eliminar elementos de la cola de prioridad
print("\nElementos eliminados en orden de prioridad:")
while not pq.is_empty():
    print(pq.dequeue())
