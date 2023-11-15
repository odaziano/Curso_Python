""" 1. Escribir un programa que calcule la suma de los primeros n números naturales y retorne el resultado"""
# resultado = 0
# for i in range(1, 10 + 1):
#     resultado += i
# print(resultado)

""" 3. Escribe un programa que reciba una cadena de texto y cuente cuántas vocales contiene.
Debe retornar el número total de vocales. Las vocales pueden ser mayúsculas o minúsculas."""

# cadena = "AEoIUpnFra"
# print(cadena.lower())
# vocales = ["a", "e", "i", "o", "u"]
# # cuenta = 0
# # vocal = 0
# # while vocales[vocal] in cadena.lower():
# #         cuenta += cuenta+1
# print(vocales[0])
# print(len(vocales))

# texto = "Hola, mundo"
# vocales = ["a", "e", "i", "o", "u"]
# cuenta = 0
# letra = 0
# for i in range(1, len(texto) +1):
#     if texto.lower()[letra] in vocales:
#         cuenta += 1
#     letra += 1
# print(cuenta)

# lista_numeros = [3, 8, 170, 7, 12]
# mayor = 0
# for numero in lista_numeros:
#     if numero > mayor:
#         mayor = numero
#     else:
#         continue
# print(mayor)

"""Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, 
# que si intentamos dividirlos por cualquier otro número, el resultado no es entero.
# Dicho de otra forma, si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero."""

# lista_primos = []
# n = 40
# for i in range(2, n +1):
#     if i == 2 or i == 3 or i == 5:
#         lista_primos.append(i)
#     elif i%2 == 0 or i%3 == 0 or i%5 == 0:
#         continue
#     else:
#         lista_primos.append(i)
# print(lista_primos)
# Ejemplos
# [2, 3, 5, 7]
# [2, 3, 5, 7, 11, 13, 17, 19]

# palabra = '1237321'
# p = 0
# u = -1
# condicion = True
# for letra in range(0, len(palabra)//2 +1):
#     if palabra[p] == palabra[u]:
#         print("p", palabra[p], "u", palabra[u])
#         p += 1
#         u -=1
#         condicion = True
#     else:
#         condicion = False
#         break
# print(condicion)


""" 7. Dada una lista de nombres, crear una funcion que devuelva una lista con los nombres que empiezan con la letra recibida como parámetro."""
"""    assert ejercicio_7("A", ["Ana", "Juan", "Pedro", "Amanda", "Pablo", "Alfredo"]) == ["Ana", "Amanda", "Alfredo"]"""



# print(len(lista_nombres))
# print(lista_nombres[0][0])
# for indice, nombre in enumerate(lista_nombres):
#     print(indice, nombre)
# lista_nombres = ["Ana", "Juan", "Pedro", "Amanda", "Pablo", "Alfredo"]
# lista_letra = []
# indice = 0
# letra = "J"
# while indice <= len(lista_nombres)-1:
#     if (lista_nombres[indice][0]) == letra:
#         lista_letra.append(lista_nombres[indice])
#         indice += 1
# print(lista_letra)


"""8. Crear una funcion que recibe un laberinto en forma de matriz y debe devolver la posicion de la salida del laberinto.
*El laberinto es una matriz donde "#" representa una pared, un espacio " " representa un pasillo y "S" representa la salida*
*Ejemplo:*

```python
laberinto = [["#","#","#","#","#","#"],
             ["#"," "," "," ","#","#"],
             ["#"," ","#"," "," ","#"],
             ["#"," ","#","#"," ","#"],
             ["#"," "," ","#"," ","#"],
             ["#","#","#","#","S","#"]]
```
La funcion debe recorrer elemento por elemento hasta encontrar la S y devolver la posicion de la S en forma de tupla (fila, columna).
*Recomendación: utilizar un bucle for anidado (un for dentro de otro for) donde el primero recorra las filas y el segundo las columnas.*"""

# laberinto = [
#         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
#         ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#"],
#         ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
#         ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
#         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
#         ["#", "#", "#", "#", "S", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
#     ]

# for f, fila in enumerate(laberinto):
#     # print(f, fila)
#     for c, columna in enumerate(fila):
#         # print(c, columna)
#         if "S" in (columna, fila):
#             print((f, c))

# print("S" in laberinto[0][0])
# print("S" in laberinto[16][14])
# print(len(laberinto))
# print(len(laberinto[0]))


# for fila in laberinto:
#     print("S" in laberinto)
#     for columna in fila:
#         print("S" in laberinto)


# LISTAS


# mi_lista = ["Argentina", "Colombia", "Perú", "Chile", "Bolivia", "Ecuador"]
# print(mi_lista)         # Completa
# print(mi_lista[0])      # Primero
# print(mi_lista[-1])     # Último
# print(mi_lista[0:4])    # Rango (del 0 al 4)
# print(mi_lista[:3])     # Los 3 primeros
# print(mi_lista[-3:])    # Los 3 últimos

# print(mi_lista[:3])     # Los 3 primeros
# print(mi_lista[3:])     # Los 3 últimos

# print(len(mi_lista))    # Largo

# mi_lista[1] = "Brasil"  # Modificar
# print(mi_lista)

# mi_lista.append("Uruguay")  # Agregar al final
# print(mi_lista)

# otra_lista = ["Venezuela", "Paraguay"]  # Concatenar 2 listas
# nueva_lista = mi_lista + otra_lista
# print(nueva_lista)

# otra_mas = ["México"]   # Método extend
# nueva_lista.extend(otra_mas)
# print(nueva_lista)

# nueva_lista.insert(3, "Panamá")     # Insertar elemento en posición determinada
# print(nueva_lista)

# nueva_lista.remove("Panamá")     # Eliminar un elemento por el nombre
# print(nueva_lista)

# del nueva_lista[4]    # Eliminar un elemento por el índice, con función DEL (de Python)
# print(nueva_lista)

# mi_lista.clear()        # Vaciar la lista
# print(mi_lista)

# mi_lista = ["Argentina", "Colombia", "Perú", "Chile", "Bolivia", "Ecuador"]
# print(mi_lista)
# eliminado = mi_lista.pop(4)     # Otra forma de eleminar un elemento , si no se especifica el índice se borra el último "Y LO DEVUELVE EN UNA VARIABLE"
# print(eliminado)

# ACTIVIDAD LISTAS

"""2) Escribe una función que tome una lista y elimine los elementos duplicados, 
devolviendo una nueva lista sin duplicados. El orden de los elementos debe mantenerse."""

# lista = ["Hola", "Mundo", "Hola", "Ejercicio", "Dos", "Numero", "Dos", "Dos"]
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 2]

"""NOT IN"""
# nueva_lista = []
# for elemento in lista:
#     if elemento not in nueva_lista:
#         nueva_lista.append(elemento)
# print(nueva_lista)

"""COMPRESIÓN"""
# duplicados = [numero for numero in lista if lista.count(numero) > 1]
# print(duplicados)

"""ENUMERATE (lista con cadenas: funciona - lista con numeros se come el último 2 ???)"""
# for i, elemento in enumerate(lista):
    # print(i, elemento)
    # if lista.count(elemento) > 1:
    #     lista.remove(elemento)

# print(lista)
# nueva_lista = lista.copy()
# print(nueva_lista)  

"""3) Escribe una función que tome una lista y un elemento como argumentos,
y elimine todas las ocurrencias de ese elemento en la lista. Devuelve la lista modificada."""
# # COMPRESIÓN
# lista = [1, 2, 3, 4, 2, 5, 2]
# elemento = 2 
# # lista = ["Alfa", "Beta", "Gamma", "Epsilon", "Alfa", "Alfa"]
# # elemento = "Alfa"

# lista = [x for x in lista if x is not elemento]
# print(lista)
# lista_modificada = lista.copy()

"""4) Escribe una función que tome una lista de números como argumento y devuelva una nueva lista que 
contenga solo los números que son mayores que 0 (cero), ordenados de menor a mayor."""
"""[-3, 5, 1, 0, -1, 8, 2, 4, 3, 6]) == [1, 2, 3, 4, 5, 6, 8]"""
# numeros = [-3, 5, 1, 0, -1, 8, 2, 4, 3, 6]

# positivos = [x for x in numeros if x >0]
# positivos.sort()
# print(positivos)

"""5) Crear una función que cuente la cantidad de veces que se repite cada elemento de una lista.
Devolver un diccionario con los elementos y sus repeticiones.
> Consejo: Usar el método `count` de las listas y listas por comprensión.
["Hola", "Hola", "Mundo", "Hola", "Palabra", "Curso", "Curso"]) == {"Hola": 3, "Mundo": 1, "Palabra": 1, "Curso": 2}"""

# lista = ["Hola", "Hola", "Mundo", "Hola", "Palabra", "Curso", "Curso"]


# diccionario = {}
# for elemento in lista:
#     diccionario[elemento] = lista.count(elemento)
# print(diccionario)

# lista_de_paises = ["Argentina", "Brasil", "Uruguay"]
# copas_ganadas = [3, 5, 2]
# diccionario = {pais: copas for pais, copas icantidadn zip(lista_de_paises, copas_ganadas)} 

# for palabra in lista:
#     cuenta = lista.count(palabra)
#     print(cuenta)

# palabras = []
# palabras = [p for p in lista if p != palabras]
# print(palabras)
# mi_lista = []
# conteo = {}
# [mi_lista.append(x) for x in lista if x not in mi_lista]
# print(mi_lista)

# for elemento in lista:
#     if elemento in conteo:
#         conteo[elemento] += 1
#     else:
#         conteo[elemento] = 1
# print(conteo)

"""6) Escribe una función que tome un número entero positivo n como argumento y devuelva una lista de los primeros n números primos.
> Nota: Un número primo es un número natural mayor que 1 que es divisible únicamente por 1 y por sí mismo."""

# n = 20
# primos = []
# for i in range(2, n):
#     if i == 2 or i == 3 or i == 5:
#         primos.append(i)
#     elif i%2 == 0 or i%3 == 0 or i%5 == 0:
#         continue
#     else:
#         primos.append(i)
# print(primos)


"""7) Escribe una función que tome una lista de números como argumento y devuelva
 `True` si la lista está ordenada en orden descendente y `False` en caso contrario."""
# numerosF = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numerosT = [11, 9, 6, 3, 1]

# if numerosT == sorted(numerosT, reverse = True):
#     print(True)
# else:
#     print(False)

"""PPI_carrito_compras"""

