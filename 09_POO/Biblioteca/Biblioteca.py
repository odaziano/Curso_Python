"""Sistema de Biblioteca
Crea una clase llamada Libro con los siguientes atributos:
- titulo
- autor
- año_publicacion
- disponible (inicializado en True)
- unidades

Crea otra clase llamada Biblioteca que tenga una lista de libros disponibles. Implementa métodos para:
- Mostrar todos los libros disponibles.
- Prestar un libro (cambia el estado de disponible a False).
- Recibir un libro (cambia el estado de disponible a True).

Por último, crear un sistema que permita seleccionar entre bibliotecas (crear al menos 2) y agregar o quitar libros de las mismas.
El sistema debe permitir guardar la base de libros de la biblioteca en un archivo JSON, o crear nuevas bibliotecas a partir de un archivo JSON."""


import os
import json
from colores import color


def limpiar_consola():
    os.system('cls')
limpiar_consola()


class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
        print(f"Libros disponibles en {self.nombre}:")
        for libro in self.libros_disponibles:
            print(f"- {libro.titulo} ({libro.autor})")

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible and libro.unidades > 0:
                libro.disponible = False
                libro.unidades -= 1
                print(f"Libro '{libro.titulo}' prestado de {self.nombre}.")
                return
        print(f"El libro '{titulo}' no está disponible en {self.nombre}.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                libro.unidades += 1
                print(f"Libro '{libro.titulo}' devuelto a {self.nombre}.")
                return
        print(f"El libro '{titulo}' no puede ser recibido en {self.nombre}.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.titulo}' agregado a {self.nombre}.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Libro '{libro.titulo}' eliminado de {self.nombre}.")
                return
        print(f"El libro '{titulo}' no existe en {self.nombre}.")

    def guardar_en_json(self, archivo):
        libros_data = []
        for libro in self.libros_disponibles:
            libros_data.append({
                'titulo': libro.titulo,
                'autor': libro.autor,
                'año_publicacion': libro.año_publicacion,
                'disponible': libro.disponible,
                'unidades': libro.unidades
            })

        with open(archivo, 'w') as file:
            json.dump(libros_data, file)
        print(f"Datos de la biblioteca {self.nombre} guardados en {archivo}.")

    def cargar_desde_json(self, archivo):
        with open(archivo, 'r') as file:
            libros_data = json.load(file)

        self.libros_disponibles = []
        for libro_data in libros_data:
            libro = Libro(
                libro_data['titulo'],
                libro_data['autor'],
                libro_data['año_publicacion'],
                libro_data['unidades']
            )
            libro.disponible = libro_data['disponible']
            self.libros_disponibles.append(libro)

        print(f"Datos de la biblioteca {self.nombre} cargados desde {archivo}.")


# Ejemplo de uso:
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca Sucursal")

libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, 5)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 3)

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)

biblioteca1.mostrar_libros_disponibles()

biblioteca1.prestar_libro("El señor de los anillos")

biblioteca1.mostrar_libros_disponibles()

biblioteca1.guardar_en_json("bibliotecaGC.json")

biblioteca2.cargar_desde_json("bibliotecaGC.json")

biblioteca2.mostrar_libros_disponibles()




# Menú Principal
def Biblioteca():
    print(color["celeste"] + color["negrita"] + "==================")
    print("BIBLIOTECA CENTRAL")
    print("==================" + color["back"])
    
    
    
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