"""# Proyectos - Parte 2
El juego debe tener las siguientes características:
1. Clases de Personajes:
    - Guerrero
    - Mago
    - Arquero
    - Asesino
 
    Estas clases deben heredar de una clase padre llamada Personaje
    
2. Atributos de Personaje:
    - Nombre
    - Vida
    - Ataque
    - Defensa
    - Inteligencia
    - Agilidad
    - Fuerza
    
    Pueden incluir nuevos atributos de ser necesario.
    
3. Métodos de Ataque:
    - El juego debe contener al menos 2 armas exclusivas para cada clase.
    - Implementa un método de ataque para cada clase que calcule el daño infligido al enemigo, teniendo en cuenta
      la defensa del enemigo, y los atributos propios del personaje, es decir:
        - Guerrero (influye su fuerza y su ataque base + ataque del arma)
        - Mago (influye su inteligencia y su ataque base + ataque del arma)
        - Arquero (influye su agilidad y su ataque base + ataque del arma)
        - Asesino (influye su agilidad e inteligencia, y su ataque base + ataque del arma)
    - Los ataques deberán ser controlados mediante un sistema de turnos, en el cual el personaje con mayor agilidad
      será el primero en atacar.
    - Cualquier mecánica adicional es bienvenida.
4. Enemigos:
    - Crea cuatro tipos de enemigos correspondientes a las clases de personajes, pero con un nombre diferente.
      Uno de los enemigos debe tener la capacidad de volar (pueden utilizar herencia múltiple para esto),
      lo cual le da la ventaja de esquivar algunos ataques.
5. Mecánica de Juego:
    - El jugador debe seleccionar su clase y empieza el juego, debe iniciar con estadísticas base.
    - Cada partida tendrá una duración establecida por ustedes, deben producirse al menos 4 encuentros."""


import random
import time
import os


def limpiar_consola():
    os.system('cls')
limpiar_consola()


class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, arma=None):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.arma = arma

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 100, 20, 10, 5, 5, 15, arma = "Espada")

    def atacar(self, enemigo, arma):
        # Bono de ataque del arma
        bono_arma = 5
        # Cálculo del daño: Fuerza del guerrero + Ataque base + Ataque del arma - Defensa del enemigo
        danio = self.fuerza + self.ataque + bono_arma - enemigo.defensa
        # Daño mínimo 0
        danio = max(0, danio)
        # Daño al enemigo
        enemigo.vida -= danio
        print(f"{self.nombre} ataca con su {arma} y causa {danio} puntos de daño a {enemigo.nombre}.")


class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 80, 15, 5, 20, 5, 10, arma = "Barita")

    def atacar(self, enemigo, arma):
        bono_arma = 5
        danio = self.fuerza + self.ataque + bono_arma - enemigo.defensa
        danio = max(0, danio)
        enemigo.vida -= danio
        print(f"{self.nombre} ataca con su {arma} y causa {danio} puntos de daño a {enemigo.nombre}.")


class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 90, 18, 8, 8, 15, 10, arma = "Flecha")

    def atacar(self, enemigo, arma):
        bono_arma = 5
        danio = self.fuerza + self.ataque + bono_arma - enemigo.defensa
        danio = max(0, danio)
        enemigo.vida -= danio
        print(f"{self.nombre} ataca con su {arma} y causa {danio} puntos de daño a {enemigo.nombre}.")


class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, 85, 17, 6, 15, 20, 12, arma = "Cuchillo")

    def atacar(self, enemigo, arma):
        bono_arma = 5
        danio = self.fuerza + self.ataque + bono_arma - enemigo.defensa
        danio = max(0, danio)
        enemigo.vida -= danio
        print(f"{self.nombre} ataca con su {arma} y causa {danio} puntos de daño a {enemigo.nombre}.")


class Enemigo(Personaje):
    def __init__(self, nombre, vuelo = random.choice([True, False])):
        # nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, arma
        super().__init__(nombre, random.randint(50, 100), random.randint(10, 20),
                         random.randint(5, 15), random.randint(5, 15),
                         random.randint(5, 15), random.randint(5, 15))
        self.vuelo = vuelo

    def atacar(self):
        # Lógica de ataque del enemigo
        danio = self.ataque - jugador.defensa
        danio = max(0, danio)
        jugador.vida -= danio
        print(f"{self.nombre} ataca y causa {danio} puntos de daño a {jugador.nombre}.")


# Crear jugador
nombre_jugador = input("Ingrese el nombre de su personaje: ")
clase_jugador = input("Seleccione su clase (Guerrero/Mago/Arquero/Asesino): ").capitalize()

if clase_jugador == "Guerrero":
    jugador = Guerrero(nombre_jugador)
elif clase_jugador == "Mago":
    jugador = Mago(nombre_jugador)
elif clase_jugador == "Arquero":
    jugador = Arquero(nombre_jugador)
elif clase_jugador == "Asesino":
    jugador = Asesino(nombre_jugador)
else:
    print("Clase no válida. Selecciona entre Guerrero, Mago, Arquero o Asesino.")
    exit()


# Crear enemigos
enemigos = [
    Enemigo("Orco"),
    Enemigo("Esqueleto"),
    Enemigo("Dragón", vuelo=True),
    Enemigo("Demonio")
]

# Iniciar enfrentamientos
num_encuentros = 4
for i in range(num_encuentros):
    print(f"\n----- Encuentro {i + 1} -----")
    enemigo_actual = random.choice(enemigos)
    while jugador.vida > 0 and enemigo_actual.vida > 0:
        print("A: ", jugador.nombre, "le quedan", jugador.vida, "vidas.")
        print("A: ", enemigo_actual.nombre, "le quedan", enemigo_actual.vida, "vidas.")
        # Lógica del turno
        if jugador.agilidad >= enemigo_actual.agilidad:
            jugador.atacar(enemigo_actual, jugador.arma)
            if enemigo_actual.vida > 0:
                enemigo_actual.atacar()
        else:
            enemigo_actual.atacar()
            if jugador.vida > 0:
                jugador.atacar(enemigo_actual, jugador.arma)
        if enemigo_actual.vida <= 0:
            print(f"{enemigo_actual.nombre} ha sido derrotado. ¡Ganaste!")
            break
        if jugador.vida <= 0:
            print(f"{jugador.nombre} ha sido derrotado. Fin del juego.")
            break
        time.sleep(3)
print("Fin del Juego")
