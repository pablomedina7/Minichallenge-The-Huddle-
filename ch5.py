#Camino más corto: 
from collections import deque

# Definición del grafo usando una lista de adyacencia
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 3],
    3: [1, 2, 4],
    4: [1, 3]
}

# Función para encontrar el camino más corto usando BFS
def shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (vertex, path) = queue.popleft()
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    
    return None

# Ejemplo de uso
start_node = 0
end_node = 4
print(f"El camino más corto desde el nodo {start_node} al nodo {end_node} es:")
camino = shortest_path(graph, start_node, end_node)
print(camino)
