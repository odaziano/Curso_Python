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


""" Menú Principal"""
def mostrar_menu():
    print("Menú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver lista de compras")
    print("4. Finalizar compra")
    print("5. Salir")


""" Lista de productos """
productos = [
    {"item": 1, "descripcion": "Leche", "valor": 50.00},
    {"item": 2, "descripcion": "Galletas", "valor": 35.00},
    {"item": 3, "descripcion": "Gaseosa", "valor": 87.00},
    {"item": 4, "descripcion": "Huevos", "valor": 66.00},
    {"item": 5, "descripcion": "Aceite", "valor": 110.00},
    {"item": 6, "descripcion": "Pan", "valor": 20.00},
]


""" Mostrar lista de productos disponibles"""
def mostrar_menu_productos():
    for producto in productos:
        print(f"Ítem: {producto['item']}, Descripción: {producto['descripcion']}, Valor: ${producto['valor']:.2f}")


""" Mostrar ticket con los productos del carrito"""
ticket = []
def mostrar_ticket():
    pass


""" Opción Agregar producot """
def Agregar_producto():
    ticket = []
    while True:
        mostrar_menu_productos()
        seleccion_producto = input("Ingrese el ítem del producto que desea: ")
        ticket.append(seleccion_producto)
        print(ticket)



def opcion_2():
    print("Seleccionaste la Opción 2.")
    # Aquí va la lógica para la Opción 2
def opcion_3():
    print("Seleccionaste la Opción 3.")
    # Aquí va la lógica para la Opción 3
def opcion_4():
    print("Seleccionaste la Opción 4.")
    # Aquí va la lógica para la Opción 4

# Menú principal
while True:
    mostrar_menu()
    seleccion = input("Ingrese el número de la opción que desea: ")
    if seleccion == "1":
        Agregar_producto()
    elif seleccion == "2":
        opcion_2()
    elif seleccion == "3":
        opcion_3()
    elif seleccion == "4":
        opcion_4()
    elif seleccion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")






























"""
En Python, :.2f es una especificación de formato que se utiliza al formatear números en una cadena (string). Esta especificación controla la cantidad de dígitos que se mostrarán después del punto decimal cuando se formatea un número en punto flotante.
:: Marca el comienzo de la especificación de formato.
.2: Indica que se deben mostrar dos dígitos después del punto decimal.
f: Indica que el número es un número de punto flotante"""