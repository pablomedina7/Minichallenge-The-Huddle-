#Ordenamiento simple:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#uso
lista = [64, 34, 25, 12, 22]
print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)
