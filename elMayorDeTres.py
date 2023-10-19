n1 = int(input("Ingrese n1: "))
n2 = int(input("Ingrese n2: "))
n3 = int(input("Ingrese n3: "))
if n1 > n2 and n1 > n3:
    print("El mayor es N1: "+str(n1))
elif n2 > n1 and n2 > n3 :
    print("El mayor es N2: "+str(n2))
else:
    print("El mayor es N3: "+str(n3))
