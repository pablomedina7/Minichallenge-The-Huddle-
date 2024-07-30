#Eliminar duplicados: 
def eliminar_duplicados(lista):
    # Convertir la lista a un conjunto para eliminar duplicados
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

# Lista de 10 enteros con duplicados
lista_con_duplicados = [1, 2, 2, 3, 4, 5, 2, 3, 4, 6, 7]

# Llamar a la función para eliminar duplicados
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)

# Mostrar la lista sin duplicados
print("Lista original con duplicados:")
print(lista_con_duplicados)
print("\nLista sin duplicados:")
print(lista_sin_duplicados)
