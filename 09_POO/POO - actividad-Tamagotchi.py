"""# ACTIVIDAD
### **Ejercicio: Tamagotchi**
Crea una clase llamada **`Tamagotchi`** que tenga los siguientes atributos:

- **`nombre`**
- **`nivel_energia`** (inicializado en 100)
- **`nivel_hambre`** (inicializado en 0)
- **`nivel_felicidad`** (inicializado en 50)
- `**humor`** (enojado, triste, indiferente, feliz, eufórico) *depende de `**nivel_felicidad**`
- **`esta_vivo`** (inicializado en True)

> Pueden agregar más atributos si lo consideran necesario.

La clase Tamagotchi debe tener los siguientes métodos:

1. **`mostrar_estado`**: Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
2. **`alimentar`**: Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
3. **`jugar`**: Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
4. **`dormir`**: Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.
5. **`bañanrse`**: Aumenta el nivel de limpieza a 30 y disminuye su felicidad en 3.

Además, implementa un método llamado **`verificar_estado`** que revise si el Tamagotchi está vivo.
Un Tamagotchi está vivo mientras su nivel de energía sea mayor que cero.
Si el nivel de hambre llega a 20, cada vez que se realice una acción que no sea `**alimentar**` deberá.
    - reducir energía en 20 puntos
    - reducir felicidad en 30 puntos.
Si el nivel de energía llega a cero, el Tamagotchi muere y el atributo **`esta_vivo`** debe ser False.

> Pueden agregar otros métodos si desean.>""" 

import random
import time
import os
from PIL import Image
import cv2
import string
from colores import color

# imagen = Image.open("kuchipatchi.png")
# imagen.show()
# imagen = cv2.imread("kuchipatchi.png", cv2.IMREAD_UNCHANGED)
# cv2.imshow("Imagen", imagen)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

def limpiar_consola():
    os.system('cls')
limpiar_consola()

# def mostrar_imagen():
#     # # Leer la imagen
#     # imagen = cv2.imread("kuchipatchi.png")
#     # # Crear la ventana con un nombre y tamaño específicos
#     # cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
#     # # Establecer el tamaño de la ventana
#     # cv2.resizeWindow("Imagen", 800, 600)
#     # # Establecer la propiedad de la ventana para que esté en primer plano
#     # cv2.setWindowProperty("Imagen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     # # Mostrar la imagen
#     # cv2.imshow("Imagen", imagen)
#     # # Esperar durante 5 segundos (5000 milisegundos)
#     # tiempo_espera = 5000  # en milisegundos
#     # cv2.waitKey(tiempo_espera)
#     # # Cerrar la ventana después del tiempo de espera
#     # cv2.destroyAllWindows()

#     imagen = cv2.imread("kuchipatchi.png", cv2.IMREAD_UNCHANGED)
#     cv2.imshow("Imagen", imagen)
#     cv2.waitKey(5000)
#     cv2.destroyAllWindows()

# mostrar_imagen()


_humor = ["enojado", "triste", "indiferente", "feliz", "eufórico"] # depende de nivel_felicidad


class Tamagotchi:
    def __init__(self, _nombre):
        self.nombre = _nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 50
        self.limpieza = 30
        self.humor = _humor[4] 
        self.vive = True
    def alimentar(self):
        # hambre - 10 y energía - 15.
        if self.energia > 0:
            print(f'\n{self.nombre} está comiendo.')
            self.energia -= 15
            self.hambre -= 20
            self.limpieza -= 5
            # mostrar_imagen()
        else:
            print(f'\n{self.nombre} no tiene suficiente energía para comer.')
    def jugar(self):
            # felicidad + 20, energía - 18 y hambre + 10
            if self.energia > 10:
                print(f'\n{self.nombre} está jugando.')
                self.felicidad += 20
                self.energia -= 18
                self.hambre += 10
                self.limpieza -= 5
            else:
                print(f'\n{self.nombre} no tiene suficiente energía para jugar.')
    def dormir(self):
        # energía + 40 y hambre + 5
        if self.limpieza <= 0:
            print(f'\n{self.nombre} tiene que bañarse!.')
        else:
            print(f'\n{self.nombre} está durmiendo.')
            self.energia += 40
            self.hambre += 5
    def bañarse(self):
        # limpieza = 30 felicidad -20
        print(f'\n{self.nombre}se está bañando.')
        self.limpieza == 30
        self.felicidad -= 20
    def estado(self):
        # nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
        if self.energia <= 0 or self.hambre >= 100:
            print(f'\n{self.nombre} ha muerto de hambre o agotamiento. ¡Fin del juego!')
            self.esta_vivo = False
        elif self.felicidad == 50:
            self.humor = _humor[4]
        elif self.felicidad == 40:
            self.humor = _humor[3]
        elif self.felicidad == 30:
            self.humor = _humor[2]
        elif self.felicidad == 20:
            self.humor = _humor[1]
        elif self.felicidad <= 0:
            self.humor = _humor[0]
            print(f'\n{self.nombre} está demasiado triste. ¡Fin del juego!')
            self.vive = False
        elif self.limpieza <= 0:
            print(f'\n{self.nombre} está demasiado sucio. ¡Fin del juego!')
            self.vive = False
        elif self.hambre == 20:
            self.energia -= 20
            self.felicidad -= 30
        else:
            print(f'Hola mi nombre es: {self.nombre}, energía: {self.energia}, hambre: {self.hambre}, felicidad: {self.felicidad}, humor: {self.humor}, limpieza: {self.limpieza}'.upper())
    def imagen(self):
        imagen = cv2.imread("kuchipatchi.png")
        cv2.imshow("Imagen", imagen)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

# Menú Principal
def jugar_tamagotchi():
    print("T A M A G O T C H I")
    nombre = input("Ingresa el nombre de tu mascota: ")
    mi_tamagotchi = Tamagotchi(nombre)
    mi_tamagotchi.estado()
    mi_tamagotchi.imagen()

    while mi_tamagotchi.vive:
        print("1. Alimentar")
        print("2. Jugar")
        print("3. Bañarse")
        print("4. Dormir")
        print("5. Estado")
        print("6. Salir del juego")
        accion = input("Elige una acción (1-6): ")

        if accion == '1':
            mi_tamagotchi.alimentar()
            # mostrar_imagen()
        elif accion == '2':
            mi_tamagotchi.jugar()
        elif accion == '3':
            mi_tamagotchi.bañarse()
        elif accion == '4':
            mi_tamagotchi.dormir()
        elif accion == '5':
            mi_tamagotchi.estado()
        elif accion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Acción no válida")

        # Simular el paso del tiempo
        time.sleep(1)

        # Verificar el estado después de cada acción
        # limpiar_consola()
        mi_tamagotchi.estado()

if __name__ == "__main__":
    jugar_tamagotchi()