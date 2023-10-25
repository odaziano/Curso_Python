lista_1 = [1, 2, 3, 4, 5]
print(lista_1)
lista_2 = lista_1.copy()
print(lista_2)
lista_3 = list(lista_2)
print(lista_3)

lista_modificada = lista_1
lista_modificada[0] = 10    # También modifica lista_1

lista_2[0] = 20             # No modifica lista_1

print("Lista 1:",lista_1,"Lista modificada:",lista_modificada)

print("Lista 2:",lista_2,"Lista 3:",lista_3)