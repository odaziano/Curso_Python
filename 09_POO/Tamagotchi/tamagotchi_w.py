"""### Ejercicio: Tamagotchi
Crea una clase llamada Tamagotchi que tenga los siguientes atributos:
ATRIBUTOS
=========
- nombre
- energia (inicializado en 100)
- hambre (inicializado en 0)
- felicidad (inicializado en 50)
- humor (enojado, triste, indiferente, feliz, eufórico) *depende de nivel_felicidad
- vive (inicializado en True)
- limpieza (inicializado en 50)
MÉTODOS
=======
La clase Tamagotchi debe tener los siguientes métodos:
1. mostrar_estado: Muestra en consola:
    - nombre
    - energía
    - hambre
    - humor
2. alimentar:
    - hambre - 10
    - energía - 15.
3. jugar:
    - felicidad + 20
    - energía - 18
    - hambre + 10
4. dormir:
    - energía + 40
    - hambre + 5
5. bañanrse:
    - limpieza + 30
    - felicidad - 5
6. estado que revise si el Tamagotchi está vivo:
    - vive ? energía sea mayor 0
    - hambre <= 20
        Si no es alimentar:
            - energía - 20
            - felicidad - 30
    Si el nivel de energía llega a cero, el Tamagotchi muere y el atributo esta_vivo debe ser False."""


import PySimpleGUI as sg
import time

humor = ("enojado", "triste", "indiferente", "feliz", "eufórico")  # depende de nivel_felicidad

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
        print(f'\n{self.nombre} está comiendo...')
        self.hambre -= 10
        self.energia -= 15
        self.limpieza -= 5


    def jugar(self):
        # felicidad + 20, energía - 18 y hambre + 10
        print(f'\n{self.nombre} está jugando...')
        self.felicidad += 20
        self.energia -= 18
        self.hambre += 10
        self.limpieza -= 15

    def dormir(self):
        # energía + 40 y hambre + 5
        print(f'\n{self.nombre} está durmiendo...')
        self.energia += 40
        self.hambre += 5

    def bañarse(self):
        # limpieza = 30 felicidad -20
        print(f'\n{self.nombre} se está bañando.')
        self.limpieza += 10
        self.felicidad -= 20

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


    def ver_estado(self):
        if self.energia <= 0 or self.hambre >= 100:
            print(f'{self.nombre} ha muerto de hambre o agotamiento. ¡Fin del juego!')
            self.vive = False
        elif self.felicidad <= 0:
            print(f'{self.nombre} está demasiado triste... ¡Llévalo a Jugar!')
            # self.vive = False
        elif self.limpieza <= 0:
            print(f'{self.nombre} está demasiado sucio... ¡Tiene que bañarse!')
            # self.vive = False
        elif self.hambre == 20:
            self.energia -= 20
            self.felicidad -= 30
        print(f'\nEnergía: {self.energia}, \nHambre: {self.hambre}, \nFelicidad: {self.felicidad}, \nHumor: {self.ver_humor()}, \nLimpieza: {self.limpieza}\n'.upper())
        return

    def bienvenida(self):
        print(f"¡Bienvenido a Tamagotchi, {self.nombre}!")


# Interfaz gráfica con PySimpleGUI
def create_layout():
    layout = [
        # [sg.Image(r'tamagotchi.png')],
        [sg.Text("T A M A G O T C H I", font=("Helvetica", 20), justification="leftr", text_color="yellow")],
        [sg.Text("Nombre de tu mascota:", font=("Helvetica", 10), justification="left", text_color="white")]+
        [sg.InputText("", key="-NOMBRE-", size=(15, 1), justification="left", tooltip="Ingresa el nombre de tu mascota")],
        [sg.Button("Iniciar Juego")],
        [sg.Output(size=(50, 15), key="-OUTPUT-")],
        [sg.Button("Alimentar"), sg.Button("Jugar"), sg.Button("Bañarse"), sg.Button("Dormir"), sg.Button("Salir")]
    ]
    return layout


def main():
    sg.theme('DarkGrey1')
    window = sg.Window("Tamagotchi", create_layout(), resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Iniciar Juego":
            nombre = values["-NOMBRE-"]
            mi_tamagotchi = Tamagotchi(nombre)
            window["-NOMBRE-"].update(f"{nombre}")
            mi_tamagotchi.bienvenida()
            mi_tamagotchi.ver_estado()

            while mi_tamagotchi.vive:
                event, values = window.read(timeout=1000)
                if event == sg.WINDOW_CLOSED:
                    break
                if event in ('Alimentar', 'Jugar', 'Bañarse', 'Dormir'):
                    mi_tamagotchi.ver_estado()
                    window["-OUTPUT-"].update("")
                    getattr(mi_tamagotchi, event.lower())()
                    window.refresh()  # Actualizar la ventana
                    time.sleep(1)
                    mi_tamagotchi.ver_estado()
                if event == "Salir":
                    window.close()
                    break
    window.close()


if __name__ == "__main__":
    main()

