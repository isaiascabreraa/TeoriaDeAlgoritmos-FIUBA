

#Funciones de colocacion

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print("\n")


#Pre: -
#Post: -
def validar_horizontal(tablero, fila, columna, largo, demanda_filas, demanda_columnas):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    if columna + largo - 1 >= m:  #Chequeo si es posible que entre en la matriz.
        #print("Fallo en valida largo horizontal")
        return False
    if demanda_filas[fila] - largo < 0:
        #imprimir_tablero(tablero)
        #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
        #print(f"La demanda de la fila es: {demanda_filas[fila]}")
        #print("Fallo en validar demanda fila horizontal")
        return False
    for i in range(largo):
        if demanda_columnas[columna + i] - 1 < 0:
            #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
            #print(f"La demanda de la fila es: {demanda_columnas[columna + i]} - 1")
            #print("Fallo en validar demanda fila horizontal")
            #print("Fallo en validar demanda columna horizontal")
            return False
    
    if columna != 0 and tablero[fila][columna - 1] != 0:  #Chequeo si la posicion anterior no esta ocupada
        #print("Fallo en validar posicion anterior horizontal")
        return False
    if columna + largo < m and tablero[fila][columna + largo] != 0:  #Chequeo que la posicion siguiente no esta ocupada.
        #print("Fallo en validar posicion siguiente horizontal")
        return False
    
    for i in range(largo):  #Chequeo que las posiciones por arriba, por debajo y a lo largo no esten ocupadas.
        if fila != 0 and fila < n - 1:
            if tablero[fila - 1][columna + i] != 0 or tablero[fila + 1][columna + i] != 0:
                #print("Fallo en superiores e inferiores horizontal")
                return False
        elif fila != 0 and fila == n - 1:
            if tablero[fila - 1][columna + i] != 0:
                #print("Fallo en superiores e inferiores horizontal")
                return False
        elif fila == 0 and fila < n - 1:
            if tablero[fila + 1][columna + i] != 0:
                #print("Fallo en superiores e inferiores horizontal")
                return False
        if tablero[fila][columna + i] != 0:  #Chequeo que no esten ocupados los lugares internos
            #print("Fallo en interiores horizontal")
            return False

    cota_derecha = columna + largo - 1
    cota_izquierda = columna

    # Verificar la diagonal superior derecha
    if cota_derecha < m - 1:  # Si existe derecha..
        if fila > 0:  # Si existe un arriba..
            if tablero[fila - 1][columna + largo] != 0:  # Y es distinto de 0..
                #print("Fallo en diagonales horizontal")
                return False
        if fila < n - 1:  # Si existe un abajo..
            if tablero[fila + 1][columna + largo] != 0:  # Y es distinto de 0..
                #print("Fallo en diagonales horizontal")
                return False

    # Verificar la diagonal inferior izquierda
    if cota_izquierda > 0:  # Si existe izquierda..
        if fila - 1 >= 0:  # Si existe un arriba..
            if tablero[fila - 1][columna - 1] != 0:  # Y es distinto de 0..
                #print("Fallo en diagonales horizontal")
                return False
        if fila + 1 < n:  # Si existe un abajo..
            if tablero[fila + 1][columna - 1] != 0:  # Y es distinto de 0..
                #print("Fallo en diagonales horizontal")
                return False
        
    return True

#Pre: -
#Post: -
def validar_vertical(tablero, fila, columna, largo, demanda_filas, demanda_columnas):
    n = len(demanda_filas)
    m = len(demanda_columnas)

    if fila + largo - 1 >= n:  #Chequeo si es posible que entre en la matriz.
        #print("Fallo en largo vertical")
        return False
    if demanda_columnas[columna] - largo < 0:
        #print("Fallo en demanda columna vertical")
        return False
    for i in range(largo):
        if demanda_filas[fila + i] - 1 < 0:
            #print("Fallo en demanda fila vertical")
            return False
    
    if fila != 0 and tablero[fila - 1][columna] != 0:  #Chequeo que la posicion anterior no este ocupada.
        #print("Fallo en anterior vertical")
        return False
    if fila + largo < n and tablero[fila + largo][columna] != 0:  #Chequeo que la posicion siguiente no esta ocupada.
        #print("Fallo en siguiente vertical")
        return False
    
    for i in range(largo):  #Chequeo que las posiciones por izquierda, por derecha y a lo largo no esten ocupadas.
        
        if tablero[fila + i][columna] != 0:  #Chequeo que no esten ocupados los lugares internos
            #imprimir_tablero(tablero)
            #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
            #print("Fallo en interiores vertical")
            return False
        
        if columna != 0 and columna < m - 1:
            if tablero[fila + i][columna - 1] != 0 or tablero[fila + i][columna + 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en superiores e inferiores vertical")
                return False
        elif columna != 0 and columna == m - 1:
            if tablero[fila + i][columna - 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en superiores e inferiores vertical")
                return False
        elif columna == 0 and columna < m - 1:
            if tablero[fila + i][columna + 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en superiores e inferiores vertical")
                return False


    cota_superior = fila + largo - 1
    cota_inferior = fila

    # Verificar la diagonal inferior izquierda y derecha
    if cota_superior < n - 1:
        if columna - 1 >= 0:
            if tablero[fila + largo][columna - 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en diagonales vertical")
                return False
        if columna + 1 < m:
            if tablero[fila + largo][columna + 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en diagonales vertical")
                return False

    # Verificar la diagonal superior izquierda y derecha
    if cota_inferior > 0:
        if columna - 1 >= 0:
            if tablero[fila - 1][columna - 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en diagonales vertical")
                return False
        if columna + 1 < m:
            if tablero[fila - 1][columna + 1] != 0:
                #imprimir_tablero(tablero)
                #print(f"Quiero poner una elemento vertical en Fila: {fila} - Columna: {columna}, de largo: {largo}")
                #print("Fallo en diagonales vertical")
                return False

    return True

import unittest

class TestValidarHorizontal(unittest.TestCase):

        ########################################### HORIZONTAL ###########################################

    def test_barco_encaja_perfectamente(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_horizontal(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_demanda_fila(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [3, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_demanda_columna(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [0, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_limite_derecho(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 0, 2, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_anterior(self):
        tablero = [
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 0, 2, 2, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_siguiente(self):
        tablero = [
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 0, 1, 2, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_superior(self):
        tablero = [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 2, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_inferior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 1, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_interna(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 1, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_diagonal_superior_derecha(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 3, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_diagonal_inferior_izquierda(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 1, 1, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_superior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 3, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_inferior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 2, 1, 3, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_superior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_horizontal(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_inferior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_horizontal(tablero, 3, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_bordes_laterales(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_horizontal(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_diagonal_superior_izquierda(self):
        tablero = [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_horizontal(tablero, 2, 1, 3, demanda_filas, demanda_columnas))


    def test_barco_encaja_con_demanda_exacta(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [2, 2, 2, 2]
        demanda_columnas = [2, 2, 2, 2]
        self.assertTrue(validar_horizontal(tablero, 0, 0, 2, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_demanda_insuficiente(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [1, 1, 1, 1]
        demanda_columnas = [1, 1, 1, 1]
        self.assertFalse(validar_horizontal(tablero, 0, 0, 2, demanda_filas, demanda_columnas))

    ########################################### VERTICAL ###########################################

    def test_barco_encaja_perfectamente(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_vertical(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_demanda_fila(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 0, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_demanda_columna(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [3, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_limite_inferior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 2, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_anterior(self):
        tablero = [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 2, 0, 2, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_siguiente(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 0, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_izquierda(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 1, 2, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_derecha(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 1, 1, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_ocupacion_interna(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 1, 2, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_diagonal_superior_derecha(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 2, 3, demanda_filas, demanda_columnas))

    def test_barco_no_encaja_por_diagonal_inferior_izquierda(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertFalse(validar_vertical(tablero, 0, 1, 2, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_izquierdo(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_vertical(tablero, 0, 0, 4, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_derecho(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [1, 1, 1, 1]
        demanda_columnas = [2, 1, 0, 4]
        self.assertTrue(validar_vertical(tablero, 0, 3, 4, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_superior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_vertical(tablero, 0, 0, 1, demanda_filas, demanda_columnas))

    def test_barco_encaja_en_borde_inferior(self):
        tablero = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        demanda_filas = [4, 4, 4, 4]
        demanda_columnas = [4, 4, 4, 4]
        self.assertTrue(validar_vertical(tablero, 3, 0, 1, demanda_filas, demanda_columnas))

if __name__ == '__main__':
    unittest.main()