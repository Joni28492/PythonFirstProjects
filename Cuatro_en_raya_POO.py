from IPython.display import clear_output


class CuatroEnRaya:

    def __init__(self, filas, columnas):
        """inicializa el estado de la clase."""
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()
        self._turno = None

    def crear_tablero(self):
        tablero = [None] * self._filas
        for f in range(self._filas):
            tablero[f] = ['.'] * self._columnas
        return tablero

    def mostrar_tablero(self):
        # Sacamos por pantalla la cabecera
        for num in range(self._columnas):
            print(num, end='  ')
        # Sacamos por pantalla el tablero
        for fila in self._tablero:
            print("")
            for casilla in fila:
                print(casilla, end="  ")

    def introducir_ficha(self, columna, color):
        """Esta funcion introduce una ficha en el tablero indicado."""
        if columna >= self._columnas or columna < 0:
            print("ERROR: Numero de columna fuera del rango.")
        elif self._tablero[0][columna] != '.':
            print("ERROR: La columna esta llena de fichas")
        else:
            for fila in range(self._filas - 1, -1, -1):
                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = color
                    return

    def _revisar_filas(self, color):
        # Recorremos las filas en busca de 4 en raya
        for r in range(self._filas):
            for c in range(self._columnas - 3):
                if self._tablero[r][c] == color and self._tablero[r][c + 1] == color and self._tablero[r][
                    c + 2] == color and self._tablero[r][c + 3] == color:
                    return True

    def _revisar_columnas(self, color):
        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columnas):
            for r in range(self._filas - 3):
                if self._tablero[r][c] == color and self._tablero[r + 1][c] == color and self._tablero[r + 2][
                    c] == color and self._tablero[r + 3][c] == color:
                    return True

    def _revisar_diagonal_derecha(self, color):

        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columnas - 3):
            for r in range(self._filas - 1, 2, -1):
                if self._tablero[r][c] == color and self._tablero[r - 1][c + 1] == color and self._tablero[r - 2][
                    c + 2] == color and self._tablero[r - 3][c + 3] == color:
                    return True

    def _revisar_diagonal_izquierda(self, color):
        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columnas - 1, 2, -1):
            for r in range(self._filas - 1, 2, -1):
                if self._tablero[r][c] == color and self._tablero[r - 1][c - 1] == color and self._tablero[r - 2][
                    c - 2] == color and self._tablero[r - 3][c - 3] == color:
                    return True

    def comprobar_ganador(self, color):
        """Comprueba si se ha producido un cuatro en raya."""
        return self._revisar_filas(color) or self._revisar_columnas(color) or self._revisar_diagonal_derecha(
            color) or self._revisar_diagonal_izquierda(color)

    def jugar(self, player1='X', player2='O'):
        """Juego main"""
        self._turno = player2
        while True:
            self._turno = player1 if self._turno == player2 else player2
            self.mostrar_tablero()
            columna = int(input("Turno del jugador {}:".format(self._turno)))
            self.introducir_ficha(columna, self._turno)
            clear_output(wait=False)
            if self.comprobar_ganador(self._turno):
                print("\n\nGanador el jugador {}!!\n\n".format(self._turno))
                self.mostrar_tablero()
                break


juego = CuatroEnRaya(6,7)
juego.jugar()