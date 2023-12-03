"""# ACTIVIDAD
### **Ejercicio: Tamagotchi**
Crea una clase llamada **Tamagotchi** que tenga los siguientes atributos:
ATRIBUTOS
=========
- **nombre**
- **energia** (inicializado en 100)
- **hambre** (inicializado en 0)
- **felicidad** (inicializado en 50)
- **humor** (enojado, triste, indiferente, feliz, eufórico) *depende de **nivel_felicidad**
- **vive** (inicializado en True)
- **limpieza** (inicializado en 50)
MÉTODOS
=======
La clase Tamagotchi debe tener los siguientes métodos:
1. **mostrar_estado**: Muestra en consola:
    - nombre
    - energía
    - hambre
    - humor
2. **alimentar**:
    - hambre - 10
    - energía - 15.
3. **jugar**:
    - felicidad + 20
    - energía - 18
    - hambre + 10
4. **dormir**:
    - energía + 40
    - hambre + 5
5. **bañanrse**:
    - limpieza + 30
    - felicidad - 5
6. **estado** que revise si el Tamagotchi está vivo:
    - vive ? energía sea mayor 0
    - hambre <= 20
        Si no es alimentar:
            - energía - 20
            - felicidad - 30
    Si el nivel de energía llega a cero, el Tamagotchi muere y el atributo **esta_vivo** debe ser False.
""" 


import random
import time
import os
from PIL import Image
import cv2
import string
import screeninfo
from colores import color


def limpiar_consola():
    os.system('cls')
limpiar_consola()


humor = ("enojado", "triste", "indiferente", "feliz", "eufórico") # depende de nivel_felicidad


class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.hambre = 0
        self.felicidad = 50
        self.limpieza = 30
        self.humor = humor[4] 
        self.vive = True
        
    def alimentar(self):
        # hambre - 10 y energía - 15.
        print(f'\n{self.nombre} está comiendo.')
        self.hambre -= 10
        self.energia -= 15
        self.limpieza -= 5
        # self.mostrar_imagen_mensaje("comiendo.jpg", "Estoy comiendo!")

    def jugar(self):
        # felicidad + 20, energía - 18 y hambre + 10
        print(f'\n{self.nombre} está jugando.')
        self.felicidad += 20
        self.energia -= 18
        self.hambre += 10
        self.limpieza -= 15
        # self.mostrar_imagen_mensaje("jugando.jpg", "Estoy jugando!")

    def dormir(self):
        # energía + 40 y hambre + 5
        if self.limpieza <= 0:
            print(f'\n{self.nombre} tiene que bañarse!.')
        else:
            print(f'\n{self.nombre} está durmiendo.')
            self.energia += 40
            self.hambre += 5
            # self.mostrar_imagen_mensaje("durmiendo.jpg", "Estoy durmiendo!")

    def bañarse(self):
        # limpieza = 30 felicidad -20
        print(f'\n{self.nombre} se está bañando.')
        self.limpieza += 10
        self.felicidad -= 20
        # self.mostrar_imagen_mensaje("bañandose.jpg", "Me estoy bañando!")

    def ver_humor(self):
        if self.felicidad >= 50:
            return humor[4]  # Eufórico
        elif 40 >= self.felicidad < 50:
            return humor[3]  # Feliz
        elif 30 >= self.felicidad < 40:
            return humor[2]  # Contento
        elif 20 >= self.felicidad < 30:
            return humor[1]  # Indiferente
        elif self.felicidad < 20:
            return humor[0]  # Triste
    
    def mostrar_estado(self):
        # nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
        if self.energia <= 0 or self.hambre >= 100:
            print(f'\n{self.nombre} ha muerto de hambre o agotamiento. ¡Fin del juego!')
            self.vive = False
        elif self.felicidad <= 0:
            print(f'\n{self.nombre} está demasiado triste. ¡Fin del juego!')
            self.vive = False
        elif self.limpieza <= 0:
            print(f'\n{self.nombre} está demasiado sucio. ¡Fin del juego!')
            self.vive = False
        elif self.hambre == 20:
            self.energia -= 20
            self.felicidad -= 30
        else:
            print(f'\nEnergía: {self.energia}, \nHambre: {self.hambre}, \nFelicidad: {self.felicidad}, \nHumor: {self.ver_humor()}, \nLimpieza: {self.limpieza}\n'.upper())
            return
    
    def mostrar_imagen_mensaje(self, imagen_path, mensaje):
        # Seleccionar la imagen
        imagen = cv2.imread(imagen_path, cv2.IMREAD_UNCHANGED)
        # Obtener la información de la pantalla
        screen_info = screeninfo.get_monitors()[0]
        screen_width, screen_height = screen_info.width, screen_info.height
        # Calcular las coordenadas para centrar la ventana
        window_x = (screen_width - imagen.shape[1]) // 2
        window_y = (screen_height - imagen.shape[0]) // 2
        # Añadir texto a la imagen
        texto = self.mostrar_estado()
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 0) # Color formato BGR azul
        grosor = 2
        tamaño_texto = 0.5
        cv2.putText(imagen, mensaje, (10, 380), font, tamaño_texto, color, grosor, cv2.LINE_AA)
        # Mostrar la imagen en la ventana y centrarla
        cv2.imshow("Imagen", imagen)
        cv2.moveWindow("Imagen", window_x, window_y)
        # Establecer la ventana en primer plano
        cv2.setWindowProperty("Imagen", cv2.WND_PROP_TOPMOST, 1)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()


# Menú Principal
def jugar_tamagotchi():
    print(color["amarillo"] + color["negrita"] + "=======================")
    print("  T A M A G O T C H I   ")
    print("   Pikachu invitado!")
    print("=======================" + color["back"])
    nombre = input(color["naranja"] + "Ingresa el nombre de tu mascota: " + color["back"])
    mi_tamagotchi = Tamagotchi(nombre)
    mi_tamagotchi.mostrar_imagen_mensaje("Pikachu_bienvenida.jpg", f"Bienvenido/a !!! : {nombre}")

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

        elif accion == '2':
            mi_tamagotchi.jugar()
        elif accion == '3':
            mi_tamagotchi.bañarse()
        elif accion == '4':
            mi_tamagotchi.dormir()
        elif accion == '5':
            mi_tamagotchi.mostrar_estado()
        elif accion == '6':
            limpiar_consola()
            print("¡Hasta luego!")
            break
        else:
            print("Acción no válida")

        # Simular el paso del tiempo
        time.sleep(1)

        # Limpiar consola y verificar el estado después de cada acción
        limpiar_consola()
        mi_tamagotchi.mostrar_estado()

if __name__ == "__main__":
    jugar_tamagotchi()