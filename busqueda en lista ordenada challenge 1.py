def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False
def ingrese_su_numero (): 
    return int(input("ingrese su numero a buscar"))
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numero_buscar = ingrese_su_numero ()
if busqueda_binaria(lista_ordenada, numero_buscar):
    print(f"El número {numero_buscar} está en la lista.")
else:
    print(f"El número {numero_buscar} no está en la lista.")