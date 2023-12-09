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
        return f"{self.titulo} - {self.autor} ({self.año_publicacion}) - Disponible: {self.disponible} - Unidades: {self.unidades}"

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
                if libro.unidades == 1:
                    libro.disponible = False
                    libro.unidades -= 1
                    sistema.guardar_json("Central.json")
                    print(f"Se ha prestado el libro: {libro.titulo} Autor: {libro.autor} Disponible: {libro.disponible}")
                    print(f"Queda/n: {libro.unidades} unidad/es disponible/s.")
                    return
                else:
                    libro.unidades -= 1
                    print(f"Se ha prestado el libro: {libro.titulo} Autor: {libro.autor} Disponible: {libro.disponible}")
                    print(f"Queda/n: {libro.unidades} unidad/es disponible/s.")
                    sistema.guardar_json("Central.json")
                    return
        print(f"No se encontró el libro {titulo} o no está disponible.")

    def recibir_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                libro.disponible = True
                libro.unidades += 1
                sistema.guardar_json("Central.json")
                print(f"Se ha recibido el libro: {libro.titulo} Autor: {libro.autor} Disponible: {libro.disponible}")
                # print(f"Se ha recibido el libro: {libro}")
                print(f"Queda/n: {libro.unidades} unidad/es disponible/s.")
                return
        print(f"No se encontró el libro {titulo} o no está prestado.")

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        sistema.guardar_json("Central.json")
        print(f"Se ha agregado el libro {libro.titulo} a la biblioteca {self.nombre}.")

    def quitar_libro(self, titulo):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo:
                if libro.unidades == 1:
                    self.libros_disponibles.remove(libro)
                    print(f"Se ha quitado el último libro: {libro.titulo} de la biblioteca {self.nombre}.")
                    return
                else:
                    libro.unidades -= 1
                    print(f"Se ha quitado una unidad del libro: {libro.titulo} de la biblioteca {self.nombre}.")
                    print(f"Queda/n: {libro.unidades} unidad/es disponible/s.")
                    return
            sistema.guardar_json("Central.json")
        print(f"No se encontró el libro {titulo} en la biblioteca {self.nombre}.")

    def crear_biblioteca_json(self, filename):
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
            json.dump(libros_json, file, indent=4)
        print(f"Se creó la Biblioteca {filename} desde la biblioteca {self.nombre}.")


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
        sistema.guardar_json("Central.json")
        print(f"Se han cargado los libros desde el archivo {filename} a la biblioteca {self.nombre}.")



sistema = Biblioteca("Central")
sistema.cargar_json("Central.json")

# Menú Principal
def MenuPpal():
    while True:
        print(Fore.GREEN + Style.BRIGHT + "=======================\n  B I B L I O T E C A  \n=======================")
        print("1. Mostrar_libros_disponibles")
        print("2. Prestar_libro")
        print("3. Recibir_libro")
        print("4. Agregar_libro")
        print("5. Quitar_libro")
        print("6. Crear_biblioteca_json")
        print("7. Cargar_json")
        print(Fore.GREEN + Style.BRIGHT + "8. Salir")
        accion = input(Fore.RED + Style.BRIGHT +"Elige una acción (1-8): ")
        print("")

        if accion == '1':   # Libros disponibles
            limpiar_consola()
            sistema.mostrar_libros_disponibles()
        elif accion == '2': # Prestar libro
            limpiar_consola()
            titulo_prestado = input("Título a prestar: ")
            sistema.prestar_libro(titulo_prestado)
            sistema.guardar_json("Central.json")
        elif accion == '3': # Recibir libro
            limpiar_consola()
            titulo_devuelto = input("Título devuelto: ")
            sistema.recibir_libro(titulo_devuelto)
            sistema.guardar_json("Central.json")
        elif accion == '4': # Agregar libro
            limpiar_consola()
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            año_publicacion = int(input("Ingrese año publicación: "))
            unidades = int(input("Ingrese unidades: "))
            titulo = Libro(titulo, autor, año_publicacion, unidades)
            sistema.agregar_libro(titulo)        
            # sistema.guardar_json("Central.json")
        elif accion == '5': # Quitar libro
            limpiar_consola()
            titulo = input("Ingrese título que desea quitar: ")
            sistema.quitar_libro(titulo)
        elif accion == '6': # Crear Biblioteca
            limpiar_consola()
            filename = input("Ingrese el nombre del la Biblioteca: ")
            sistema.crear_biblioteca_json(filename+".json")
        elif accion == '7': # Cargar JSON
            limpiar_consola()
            filename = input("Ingrese el nombre del la Biblioteca, desde donde desea agregar libros: ")
            sistema.cargar_json(filename+".json")
        elif accion == '8':
            limpiar_consola()
            print("Salió del sistema")
            break
        else:
            limpiar_consola()
            print("Acción no válida")
            

if __name__ == "__main__":
    MenuPpal()
