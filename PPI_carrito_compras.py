"""### Carrito de compras
Diseñar un programa que simule un carrito de compras, el mismo debe contar con un menú que contenga las siguientes opciones:
    1. Agregar producto
    2. Eliminar producto
    3. Ver lista de compras
    4. Finalizar compra
    5. Salir
Los productos disponibles son:
    Leche $50 - Galletas $35 - Gaseosa $87 - Huevos $66 - Aceite $110 - Pan $20
Al finalizar la compra, debe “imprimirse” el ticket de compra, el cual contendrá la lista de productos y el precio final."""


""" Limpiar consola """
import os
def limpiar_consola():
    sistema_operativo = os.name
    if sistema_operativo == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux, macOS)
        os.system('clear')
limpiar_consola()


""" Importar mi modulo color """
from PPI_color import color


""" Menú Principal"""
def menu_ppal():
    print(color["magenta"] + color["negrita"] + "=======================")
    print("  M I N I M A R K E T   ")
    print("=======================" + color["back"])
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver lista de compras")
    print("4. Finalizar compra")
    print("5. Salir")


""" Lista de productos """
productos = [
    {"codigo": "1", "descripcion": "Leche", "valor": 50.00},
    {"codigo": "2", "descripcion": "Galletas", "valor": 35.00},
    {"codigo": "3", "descripcion": "Gaseosa", "valor": 87.00},
    {"codigo": "4", "descripcion": "Huevos", "valor": 66.00},
    {"codigo": "5", "descripcion": "Aceite", "valor": 110.00},
    {"codigo": "6", "descripcion": "Pan", "valor": 20.00},
]


""" Mostrar lista de productos disponibles"""
def menu_productos():
    limpiar_consola()
    print(color["cyan"] + "=======================")
    print("Productos disponibles  ")
    print("=======================" + color["back"])
    for producto in productos:
        print(f"Código: {producto['codigo']}, Descripción: {producto['descripcion']}, Valor: ${producto['valor']:.2f}")


""" Mostrar ticket con los productos del carrito"""
ticket = {}     # Variable pública
def mostrar_ticket():
    if not ticket:
        print(color["rojo"] + "El ticket está vacío." + color["back"])
        return
    if not finalizar_compra:
        limpiar_consola()
    print("Productos en el carrito ")
    print("=======================")
    for codigo, cantidad in ticket.items():
        producto = buscar_producto("codigo", codigo)
        descripcion = producto["descripcion"]
        valor_unitario = producto["valor"]
        total_producto = valor_unitario * cantidad
        print(f"Código: {codigo}, Descripción: {descripcion}, Cantidad: {cantidad}, Valor Unitario: ${valor_unitario:.2f}, Total: ${total_producto:.2f}")


""" Buscar producto"""
def buscar_producto(criterio, valor):
    for producto in productos:
        if producto[criterio] == valor:
            return producto
    return None


""" Agregar producto  Opción 1 """
def agregar_producto():
    limpiar_consola()
    menu_productos()
    codigo_busqueda = str(input(color["naranja"] + "Ingrese el código del producto: " + color["back"]))
    resultado = buscar_producto("codigo", codigo_busqueda)
    if resultado:
        cantidad = int(input(color["naranja"] + "Ingrese la cantidad: " + color["back"]))
        if codigo_busqueda in ticket:
            ticket[codigo_busqueda] += cantidad
            lista_compras()
        else:
            ticket[codigo_busqueda] = cantidad
            lista_compras()
    else:
        limpiar_consola()
        print(color["rojo"] + f"Producto {codigo_busqueda} no encontrado." + color["back"])
        return

""" Eliminar producto  Opción 2 """
def eliminar_producto():
    limpiar_consola()
    if not ticket:
        print(color["rojo"] + "El carrito está vacío." + color["back"])
        return
    mostrar_ticket()
    codigo_eliminar = str(input(color["naranja"] + "Ingrese el código del producto que desea eliminar del ticket: " + color["back"]))
    if codigo_eliminar in ticket:
        resultado = buscar_producto("codigo", codigo_eliminar)
        cantidad_eliminar = int(input(color["naranja"] + "Ingrese la cantidad que desea eliminar: " + color["back"]))
        if cantidad_eliminar < ticket[codigo_eliminar]:
            ticket[codigo_eliminar] -= cantidad_eliminar
            lista_compras()
            print(color["rojo"] + f"Código: {resultado['codigo']}, {resultado['descripcion']}, Cantidad: {cantidad_eliminar}, (s) eliminado(s) del ticket." + color["back"])
        elif cantidad_eliminar == ticket[codigo_eliminar]:
            del ticket[codigo_eliminar]
            lista_compras()
            print(color["rojo"] + f"Código: {resultado['codigo']}, {resultado['descripcion']}(s) eliminado(s) completamente del ticket." + color["back"])
        else:
            lista_compras()
            print(color["rojo"] + "La cantidad ingresada es mayor que la cantidad en el ticket." + color["back"])
    else:
        lista_compras()
        print(color["rojo"] + "El producto no está en el ticket." + color["back"])


""" Ver lista compras  Opción 3 """
def lista_compras():
    limpiar_consola()
    mostrar_ticket()


""" Finalizar la compra Opción 4 """
def finalizar_compra():
    limpiar_consola()
    if not ticket:
        print(color["rojo"] + "El ticket está vacío. No se puede finalizar la compra." + color["back"])
        return

    total = sum(buscar_producto("codigo", codigo)["valor"] * cantidad for codigo, cantidad in ticket.items())
    print(color["verde"] + "=======================")
    print("       T I C K E T       ")
    print("=======================" + color["back"])
    mostrar_ticket()
    print(color["negro"] + color["famarillo"] + color["negrita"] + f"Total a pagar: ${total:.2f} " + color["back"])
    print(color["verde"] + "Gracias!, por su compra." + color["back"])
    ticket.clear()


""" Menú principal"""
while True:
    menu_ppal()
    seleccion = input(color["naranja"] + "Ingrese el número de la opción que desea: " + color["back"])
    if seleccion == "1":
        agregar_producto()
    elif seleccion == "2":
        eliminar_producto()
    elif seleccion == "3":
        lista_compras()
    elif seleccion == "4":
        finalizar_compra()
    elif seleccion == "5":
        limpiar_consola()
        print("Eligió salir del programa.")
        break
    else:
        print(color["rojo"] + "Opción no válida. Por favor, ingrese un número del 1 al 5." + color["back"])

