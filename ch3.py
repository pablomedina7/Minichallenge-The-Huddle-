# Recorrido en profundidad (DFS): Definición del grafo usando una lista de adyacencia
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Función para realizar DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# Ejemplo de uso
print("Recorrido DFS comenzando desde el nodo 0:")
dfs(graph, 0)
