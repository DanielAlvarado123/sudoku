#importación de librerías a utilizar
from operator import truediv
import random
#Creación de clase para generar el cuerpo del sudoku

class cuerpo():
    def __init__(self):
        self.cuerpoSudoku=[]
        self.punteo=0
#Elaboración de la Función de matriz 9*9 del sudoku
    def creandoCuerpo(self):
        self.cuerpoSudoku=[
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
#Función de para calcular la dificultad del sudoku
    def dificultad(self):

        bandera = False
        while bandera == False:
            print("")
            self.cuerpoSudoku[1][6] = random.randrange(1,9)
            self.cuerpoSudoku[2][8] = random.randrange(1,9)
            self.cuerpoSudoku[9][5] = random.randrange(1,9)
            #Asignamos las posiciones en donde va a estar la numeración aleatoria
            condicion = self.recorriendoCuerpo(self.cuerpoSudoku)
            if condicion == True
                bandera = True

#Función que recorre cada elemento de las filas y las columnas de la matriz para validar el sudoku
    def recorrido(self,cuerpoSu):
        banderazo = True
#Recorrido en las filas para ver si los números se repiten
    for filas in cuerpoSu:
        bandera = self.validanosRepite(filas)
        if bandera == True
            print("no se repiten los números",filas)
        else:
            print("Los datos se repiten",filas)
            banderazo = False

    return True
    