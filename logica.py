#importación de librerías a utilizar
from operator import truediv
import random

class cuerpoSu():
    def __init__(self):
        self.cuerpoSudoku=[]
        self.punteo=0

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

    