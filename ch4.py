#Recorrido en amplitud (BFS): 
from collections import deque
# Definición del grafo usando una lista de adyacencia
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
# Función para realizar BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Ejemplo de uso
print("Recorrido BFS comenzando desde el nodo 0:")
bfs(graph, 0)
