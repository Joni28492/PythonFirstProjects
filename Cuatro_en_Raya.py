
#from IPython.display import clear_output


def crear_tablero(filas, columnas):
    """Crea el tablero de juego.

    Parametros posicionales
    filas -- int que represente el numero de filas del tablero.
    columnas -- int que represente el numero de columans del tablero.
    """
    tablero = [None] * filas
    for f in range(filas):
        tablero[f] = ['.'] * columnas
    return tablero

def mostrar_tablero(tablero):
    """Muestra el tablero por pantalla."""
    # Sacamos por pantalla la cabecera
    for num in range(len(tablero[0])):
        print(num, end='  ')
    # Sacamos por pantalla el tablero
    for fila in tablero:
        print("")
        for casilla in fila:
            print(casilla, end="  ")
    print("\n")

def introducir_ficha(tablero, columna, color):
    """Esta funcion introduce una ficha en el tablero indicado."""
    if columna >= len(tablero[0]) or columna < 0:
        print("ERROR: Numero de columna fuera del rango.")
        return
    elif tablero[0][columna] != '.':
        print("ERROR: La columna esta llena de fichas")
        return
    else:
        for fila in range(len(tablero)-1, -1, -1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = color
                return tablero

def revisar_filas(tablero, color):
    # Obtenemos el numero de filas y columnas
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for r in range(num_filas):
        for c in range(num_columnas - 3):
            if tablero[r][c] == color and tablero[r][c+1] == color and tablero[r][c+2] == color and tablero[r][c+3] == color:
                return True

def revisar_columnas(tablero, color):
    # Obtenemos el numero de filas y columnas
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columnas):
        for r in range(num_filas - 3):
            if tablero[r][c] == color and tablero[r+1][c] == color and tablero[r+2][c] == color and tablero[r+3][c] == color:
                return True

def revisar_diagonal_derecha(tablero, color):
    # Obtenemos el numero de filas y columnas
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columnas - 3):
        for r in range(num_filas-1, 2, -1):
            if tablero[r][c] == color and tablero[r-1][c+1] == color and tablero[r-2][c+2] == color and tablero[r-3][c+3] == color:
                return True

def revisar_diagonal_izquierda(tablero, color):
    # Obtenemos el numero de filas y columnas
    num_filas = len(tablero)
    num_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for c in range(num_columnas-1, 2, -1):
        for r in range(num_filas-1, 2, -1):
            if tablero[r][c] == color and tablero[r-1][c-1] == color and tablero[r-2][c-2] == color and tablero[r-3][c-3] == color:
                return True

def comprobar_ganador(tablero, color):
    """Comprueba si se ha producido un cuatro en raya."""
    return revisar_filas(tablero, color) or revisar_columnas(tablero, color) or revisar_diagonal_derecha(tablero, color) or revisar_diagonal_izquierda(tablero, color)


tablero = crear_tablero(6, 7)
turno = 'R'
sig_turno = 'A'
while True:
    turno = sig_turno
    mostrar_tablero(tablero)
    if turno == 'R':
        columna = int(input("Turno del rojo: "))
        sig_turno = 'A'
    elif turno == 'A':
        columna = int(input("Turno del amarillo: "))
        sig_turno = 'R'
    introducir_ficha(tablero, columna, turno)
    #clear_output(wait=False)
    if comprobar_ganador(tablero, turno):
        print("Ganador el jugador ", turno, "\n\n")
        mostrar_tablero(tablero)
        break