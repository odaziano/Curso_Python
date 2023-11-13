
"""### Adivina el número (juego)
Crear un programa en el que el usuario deberá adivinar el número que la máquina escogió.
Deben utilizar la librería `random` para generar la elección de la máquina.
El usuario tendrá 5 vidas, cada vez que intente adivinar, recibirá como respuesta “El número es mayor” o
“El número es menor” según corresponda, y perderá una vida. Ganará cuando logre adivinar el número elegido por la máquina.."""

import random
def adivina_el_numero(x):


    aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x
    prediccion = 0
    intentos = 5
    while intentos > 0:
        prediccion = int(input(f"Adivina un número entre 1 y {x} (Te queda/n {intentos} intento/s) : ")) # f-string
        intentos -= 1
        if prediccion < aleatorio:
            print(f"Intenta otra vez, el número {prediccion} es menor que el aleatorio.")
        elif prediccion > aleatorio:
            print(f"Intenta otra vez, el número {prediccion} es mayor que el aleatorio.")
        elif prediccion == aleatorio:
            print(f"Felicitaciones!!!, adivinaste, el número aleatorio es: {aleatorio}.")
            break
    if intentos == 0 and prediccion != aleatorio:
        print("Se agotaron los intentos")

adivina_el_numero(10)
