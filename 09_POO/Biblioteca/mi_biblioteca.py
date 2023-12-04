"""### **Sistema de Biblioteca**
Crea una clase llamada Libro`** con los siguientes atributos:
    - titulo
    - autor
    - año_publicacion
    - disponible`** (inicializado en True)
    - unidades

Pueden crear el JSON de libros utilizando: [JSON Data AI](https://www.jsondataai.com/)

Crea otra clase llamada Biblioteca`** que tenga una lista de libros disponibles.
     Implementa métodos para:
        - Mostrar todos los libros disponibles.
        - Prestar un libro (cambia el estado de disponible`** a False).
        - Recibir un libro (cambia el estado de disponible`** a True).

Por último, crear un sistema que permita:
    - seleccionar entre bibliotecas (crear al menos 2)
    - agregar libros
    - quitar libros
    - permitir guardar la base de libros de la biblioteca en un archivo **JSON**
    - o crear nuevas bibliotecas a partir de un archivo ********JSON********.
"""

import json
import os
from datetime import datetime, timedelta
from colores import color

"""Método Limpiar consola"""
def limpiar_consola():
    os.system('cls')
limpiar_consola()

"""Clase Libro"""
class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades
    def __str__(self):
        return f"{self.titulo} ({self.autor}, {self.año_publicacion}) - Disponibles: {self.unidades}"

"""Clase Socio"""
class Socio:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = {}
    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}) - Libros Prestados: {len(self.libros_prestados)}"

"""Calase Biblioteca"""
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.socios = []


    def cargar_desde_json(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
        self.libros = [Libro(**libro_data) for libro_data in data['libros']]
        self.socios = [Socio(**socio_data) for socio_data in data['socios']]
        """
        **libro_data: Desempaqueta el diccionario libro_data. Supongamos que libro_data es un diccionario con las claves 'titulo', 'autor', 'año_publicacion', 'disponible', 'unidades'. Al utilizar **libro_data, estás pasando estos valores como argumentos de palabra clave a la clase Libro. Esencialmente, es equivalente a hacer algo como Libro(titulo=libro_data['titulo'], autor=libro_data['autor'], ...). Esto es útil cuando tienes un diccionario con los mismos nombres de clave que los parámetros de la función."""

    def guardar_en_json(self, archivo):
        libros_data = [{'titulo': libro.titulo, 'autor': libro.autor, 'año_publicacion': libro.año_publicacion,
                        'unidades': libro.unidades, 'prestados': libro.prestados} for libro in self.libros]
        socios_data = [{'nombre': socio.nombre, 'dni': socio.dni,
                        'libros_prestados': list(socio.libros_prestados.keys())} for socio in self.socios]

        data = {'libros': libros_data, 'socios': socios_data}

        with open(archivo, 'w') as file:
            json.dump(data, file)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado al sistema.")

    def dar_de_baja_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"Libro '{libro.titulo}' dado de baja del sistema.")
                return
        print(f"El libro '{titulo}' no está en el sistema.")

    def prestar_libro(self, socio_dni, titulo):
        socio = self.buscar_socio(socio_dni)
        if socio:
            libro = self.buscar_libro(titulo)
            if libro and libro.unidades > 0:
                libro.unidades -= 1
                libro.prestados += 1
                fecha_devolucion = datetime.now() + timedelta(days=14)
                socio.libros_prestados[titulo] = fecha_devolucion.strftime('%Y-%m-%d')
                print(f"Libro '{titulo}' prestado a {socio.nombre}. Fecha de devolución: {fecha_devolucion}")
            elif not libro:
                print(f"El libro '{titulo}' no está en el sistema.")
            else:
                print(f"No hay unidades disponibles del libro '{titulo}'.")
        else:
            print(f"Socio con DNI '{socio_dni}' no encontrado.")

    def devolver_libro(self, socio_dni, titulo):
        socio = self.buscar_socio(socio_dni)
        if socio and titulo in socio.libros_prestados:
            libro = self.buscar_libro(titulo)
            libro.unidades += 1
            libro.prestados -= 1
            del socio.libros_prestados[titulo]
            print(f"Libro '{titulo}' devuelto por {socio.nombre}.")
        elif not socio:
            print(f"Socio con DNI '{socio_dni}' no encontrado.")
        else:
            print(f"El socio {socio.nombre} no tiene prestado el libro '{titulo}'.")

    def listar_socios(self):
        for socio in self.socios:
            print(socio)

    def agregar_socio(self, socio):
        self.socios.append(socio)
        print(f"Socio '{socio.nombre}' agregado al sistema.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def buscar_socio(self, dni):
        for socio in self.socios:
            if socio.dni == dni:
                return socio
        return None


# Ejemplo de uso:
sistema = SistemaBiblioteca()

# Cargar datos desde un archivo JSON (si existe)
try:
    sistema.cargar_desde_json("biblioteca_data.json")
except FileNotFoundError:
    print("No se encontró un archivo de datos existente. Se creará uno nuevo.")

# Crear algunos libros y socios
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 5)
libro2 = Libro("El túnel", "Ernesto Sabato", 1948, 3)
libro3 = Libro("Rayuela", "Julio Cortázar", 1963, 2)

socio1 = Socio("Juan Pérez", "12345678")
socio2 = Socio("María Gómez", "87654321")

# Agregar libros y socios al sistema
sistema.agregar_libro(libro1)
sistema.agregar_libro(libro2)
sistema.agregar_libro(libro3)

sistema.agregar_socio(socio1)
sistema.agregar_socio(socio2)

# Prestar libros
sistema.prestar_libro("12345678", "Cien años de soledad")
sistema.prestar_libro("87654321", "El túnel")

# Listar libros y socios
print("\nLibros disponibles:")
sistema.listar_libros()

print("\nSocios:")
sistema.listar_socios()

# Devolver libros
sistema.devolver_libro("12345678", "Cien años de soledad")
sistema.devolver_libro("87654321", "El túnel")

# Guardar datos en un archivo JSON
sistema.guardar_en_json("biblioteca_data.json")


# Menú Principal
def jugar_tamagotchi():
    print(color["verde"] + color["negrita"] + "=======================")
    print("  B I B L I O T E C A   ")
    print("=======================" + color["back"])

    while True:
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
    sistema = SistemaBiblioteca()