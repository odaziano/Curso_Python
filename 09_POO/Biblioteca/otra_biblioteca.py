"""### **Sistema de Biblioteca**
Crea una clase llamada Libro con los siguientes atributos:
    - titulo
    - autor
    - año_publicacion
    - disponible (inicializado en True)
    - unidades

Pueden crear el JSON de libros utilizando: [JSON Data AI](https://www.jsondataai.com/)

Crea otra clase llamada Biblioteca que tenga una lista de libros disponibles.
     Implementa métodos para:
        - Mostrar todos los libros disponibles.
        - Prestar un libro (cambia el estado de disponible`** a False).
        - Recibir un libro (cambia el estado de disponible`** a True).

Por último, crear un sistema que permita:
    - seleccionar entre bibliotecas (crear al menos 2)
    - agregar libros
    - quitar libros
    - permitir guardar la base de libros de la biblioteca en un archivo **JSON**
    - o crear nuevas bibliotecas a partir de un archivo JSON.
"""


import json
import os
import cv2
from datetime import datetime, timedelta
from colores import color
from colorama import Fore, Back, Style, init
init(autoreset=True)

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

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año_publicacion})"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def mostrar_libros_disponibles(self):
        print(f"Libros disponibles en la biblioteca {self.nombre}:")
        for libro in self.libros_disponibles:
            print(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Se ha prestado el libro: {libro}")
                return
        print(f"No se encontró el libro {titulo} o no está disponible.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Se ha recibido el libro: {libro}")
                return
        print(f"No se encontró el libro {titulo} o no está prestado.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Se ha agregado el libro {libro.titulo} a la biblioteca {self.nombre}.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                self.libros_disponibles.remove(libro)
                print(f"Se ha quitado el libro: {libro} de la biblioteca {self.nombre}.")
                return
        print(f"No se encontró el libro {titulo} en la biblioteca {self.nombre}.")

    def guardar_json(self, filename):
        libros_json = []
        for libro in self.libros_disponibles:
            libros_json.append({
                'titulo': libro.titulo,
                'autor': libro.autor,
                'año_publicacion': libro.año_publicacion,
                'disponible': libro.disponible,
                'unidades': libro.unidades
            })

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(libros_json, file, indent=2)

    def cargar_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            libros_json = json.load(file)

        for libro_json in libros_json:
            libro = Libro(libro_json['titulo'], libro_json['autor'], libro_json['año_publicacion'], libro_json['unidades'])
            libro.disponible = libro_json['disponible']
            self.libros_disponibles.append(libro)
        print(f"Se han cargado los libros desde el archivo {filename} a la biblioteca {self.nombre}.")



sistema = Biblioteca()
try:
    sistema.cargar_json("biblioteca1.json")
except FileNotFoundError:
    print("No se encontró un archivo de datos existente. Se creará uno nuevo.")
# Ejemplo de uso del sistema de biblioteca
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca del Barrio")
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, 5)
libro2 = Libro("1984", "George Orwell", 1949, 3)
biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.mostrar_libros_disponibles()
biblioteca1.prestar_libro("Harry Potter y la piedra filosofal")
biblioteca1.mostrar_libros_disponibles()
biblioteca1.guardar_json("biblioteca1.json")
# Crear una nueva biblioteca a partir del archivo JSON
biblioteca3 = Biblioteca("Biblioteca2")
biblioteca3.cargar_json("biblioteca1.json")
biblioteca3.mostrar_libros_disponibles()



# Menú Principal
def MenuPpal():
    while True:
        print(color["verde"] + color["negrita"] + "=======================\n  B I B L I O T E C A   \n=======================" + color["back"])
        print("1. Mostrar_libros_disponibles")
        print("2. Prestar_libro")
        print("3. Recibir_libro")
        print("4. Agregar_libro")
        print("5. Quitar_libro")
        print("6. Guardar_json")
        print("7. Cargar_json")
        print(color["verde"] + color["negrita"] + "8. Salir")
        accion = input("Elige una acción (1-8): ")

        if accion == '1':
            print("\nLibros disponibles:")
            sistema.mostrar_libros_disponibles()
        elif accion == '2':
            sistema.prestar_libro()            
        elif accion == '3':
            sistema.recibir_libro()
        elif accion == '4':
            sistema.agregar_libro()
        elif accion == '5':
            sistema.quitar_libro
        elif accion == '6':
            sistema.guardar_json()
        elif accion == '7':
            sistema.cargar_json()
        elif accion == '8':
            limpiar_consola()
            print("Salió del sistema")
            break
        else:
            print("Acción no válida")
            
        # limpiar_consola()

if __name__ == "__main__":
    MenuPpal()