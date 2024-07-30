#Árbol binario de búsqueda (BST): 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Función para insertar un nuevo nodo con una clave determinada
def insert(root, key):
    # Si el árbol está vacío, devuelve un nuevo nodo
    if root is None:
        return Node(key)
    
    # De lo contrario, recorre el árbol
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    # Devuelve el (sub)árbol de nodo raíz actualizado
    return root

# Función para realizar un recorrido en orden del árbol (inorder traversal)
def inorder(root):
    if root:
        # Primero recorre el subárbol izquierdo
        inorder(root.left)
        # Luego el nodo raíz
        print(root.val, end=" ")
        # Finalmente el subárbol derecho
        inorder(root.right)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un árbol binario de búsqueda y añadir nodos
    root = None
    elements = [50, 30, 20, 40, 70]
    for element in elements:
        root = insert(root, element)
    
    # Realizar un recorrido en orden del árbol
    print("Recorrido en orden del árbol binario de búsqueda:")
    inorder(root)
