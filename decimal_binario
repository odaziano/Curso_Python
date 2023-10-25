# print(1<<2)

decimal = int(input("Ingrese un número decimal por teclado: "))

dividendo = decimal
divisor = 2
cociente = dividendo//1
resto = 0
mi_binario = []

while cociente >= 2:
    dividendo = cociente
    cociente = dividendo//divisor
    resto = dividendo%divisor
    mi_binario.append(resto)
    print("Dividendo:", dividendo,  "Cociente:", cociente , "Resto", resto)
    print(mi_binario)

mi_binario.append(cociente)
print("Dividendo:", dividendo,  "Cociente:", cociente , "Resto", resto)
print(f"\nEl número binario de {decimal} es:", mi_binario[::-1])

