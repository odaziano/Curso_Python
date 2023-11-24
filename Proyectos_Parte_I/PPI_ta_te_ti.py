""" Ta-Te-Ti
Construir un Ta-Te-Ti (tres en raya) que se juegue contra otro jugador.
El usuario deberá indicar la posición en la que desea jugar su ficha.
Deberán utilizar una matriz para simular el tablero de juego."""


""" Función: Imprime el tablero separando las casillas mediante el método join """
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")


"""Función: all verifica que todas las casillas de una línea, columna o diagonal, pertenezcan al mismo jugador."""
def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False


"""Función: Jugar
    1) Define la lista tablero (vacía)
    2) Asigna el valor "X" a el primer jugador
    3) Hará mientras sea Verdadero
        - Imprime tablero antes de la primera jugada y después de cada jugada
        - Solicita la entrada de fila y columna al jugador actual
        - Verifica que la posición de fila y columna sean valores válidos (agregado mío)
        - Verifica que la casilla esté vacía
        - Reemplaza el contenido de la casilla seleccionada por la "ficha" del jugador actual
        - Verifica por cada ciclo del bucle while si:
            - Si hay un ganador (funcion verificar_ganador) => break
            - Si hay empate, es decir si hay 6 casillas ocupadas, break
            - Cambia el jugador a "O" si es "X" y a "X" si es "O"
"""
def jugar():
    tablero = [[" " for i in range(3)] for j in range(3)]
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador_actual}, elige una columna (0, 1, 2): "))
        if fila in range(0, 3) and columna in range(0, 3):
            if tablero[fila][columna] == " ":
                tablero[fila][columna] = jugador_actual
                if verificar_ganador(tablero, jugador_actual):
                    imprimir_tablero(tablero)
                    print(f"¡Jugador {jugador_actual} gana!")
                    break
                elif all(tablero[i][j] != " " for i in range(3) for j in range(3)):
                    imprimir_tablero(tablero)
                    print("¡Empate!")
                    break
                jugador_actual = "O" if jugador_actual == "X" else "X"
            else:
                print("¡Casilla ocupada! Intenta de nuevo.")
        else:
            print(f"¡Posición fila {fila} y/o columna {columna} no válida! Intenta de nuevo.")


"""La línea if __name__ == "__main__": se utiliza para condicionar la ejecución de ciertas partes del código.
Las instrucciones debajo de esta línea se ejecutarán solo si el script está siendo ejecutado directamente y no
si está siendo importado como un módulo en otro script."""
if __name__ == "__main__":
    jugar() 