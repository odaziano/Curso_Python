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

# Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, 
# que si intentamos dividirlos por cualquier otro número, el resultado no es entero.
# Dicho de otra forma, si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.

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

laberinto = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "S", "#"]
    ]
# print("S" in laberinto[0][0])
# print("S" in laberinto[16][14])
# print(len(laberinto))
# print(len(laberinto[0]))


# filas = len(laberinto)
# columnas = len(laberinto[0])
# fila = 0
# columna = 0
# print("filas", len(laberinto), "columnas", len(laberinto[0]))
# while fila <= len(laberinto) or columna <= len(laberinto[0]):
#     if "S" in laberinto[fila][columna]:
#         print(laberinto[fila][columna])
#         fila += 1
#         columna += 1

for fila in laberinto:
    print("S" in laberinto)
    for columna in fila:
        print("S" in laberinto)