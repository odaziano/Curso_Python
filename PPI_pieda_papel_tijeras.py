"""### Piedra, Papel o Tijeras
Crear un programa que permita jugar al clásico juego piedra, papel o tijeras.
El mismo debe pedir al usuario que ingrese su jugada, y utilizando la librería `random` generar una elección para la máquina.
Luego debe mostrar el ganador y preguntar al usuario si desea volver a jugar."""

import random
opciones = ["piedra", "papel", "tijera"]
pc = random.choice(opciones)


def piedra_papel_tijera():
    print(f"Pc eligió: {pc}")
    if jugador == pc:
        print("!Empate¡") 
    elif ((jugador == "piedra" and pc == "tijera")
        or (jugador == "tijera" and pc == "papel")
        or (jugador == "papel" and pc == "piedra")):
        print("Ganó el jugador!")
    else:
        print("Ganó la PC!")


while True:
    jugador = input("Ingresa tu opción : piedra, papel o tijera : \n").lower()
    if jugador not in opciones:
        print(f"Opción inválida, debes elegir: {opciones}")
        continue
    print(f"Jugador eligió: {jugador}")
    piedra_papel_tijera()
    jugar_de_nuevo = input("Quiere jugar de nuevo? s/n: ").lower()
    if jugar_de_nuevo != "s":
        break
