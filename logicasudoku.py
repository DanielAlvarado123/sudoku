from operator import truediv
import random
import os


class cuerpo():
    def __init__(self):
        self.cuerposudoku=[]
        self.punteo=0
    
    def creandoCuerpo(self):

       self.cuerposudoku=[[0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0]]


    def dificultad(self):
        
        bandera = False
        while bandera == False:
            self.cuerposudoku[0][2]= random.randrange(1,9)
            self.cuerposudoku[2][5]= random.randrange(1,9)
            self.cuerposudoku[6][5]= random.randrange(1,9)
            self.cuerposudoku[7][8]= random.randrange(1,9)
            self.cuerposudoku[3][6]= random.randrange(1,9)
            self.cuerposudoku[6][1]= random.randrange(1,9)
            self.cuerposudoku[3][0]= random.randrange(1,9)
            self.cuerposudoku[0][2]= random.randrange(1,9)
            self.cuerposudoku[0][1]= random.randrange(1,9)
            self.cuerposudoku[6][5]= random.randrange(1,9)
            self.cuerposudoku[0][3]= random.randrange(1,9)
            self.cuerposudoku[1][3]= random.randrange(1,9)
            self.cuerposudoku[2][4]= random.randrange(1,9)
            self.cuerposudoku[2][5]= random.randrange(1,9)
            self.cuerposudoku[3][7]= random.randrange(1,9)
            self.cuerposudoku[8][0]= random.randrange(1,9)
            self.cuerposudoku[8][6]= random.randrange(1,9)
            self.cuerposudoku[8][2]= random.randrange(1,9)
            self.cuerposudoku[8][1]= random.randrange(1,9)
            self.cuerposudoku[8][8]= random.randrange(1,9)

            cumplio= self.recorrido(self.cuerposudoku)
            if cumplio == True:
                bandera=True
                
        
      
        
    #recorre todas las filas, columnas y secciones para validar si el sudoku cumple
    def recorrido(self,cuerposu):
        banderaB=True
        #-------------recorriendo filas y validando que no se repitan los numeros----------------------- 
        for filas in cuerposu:
            bandera = self.validanoserepite(filas)
            if bandera == True:
                print("no se repiten datos",filas)
            else:
                print("Se repiten los datos",filas)
               # os.system("cls")
                banderaB=False
        # codigo para recorre filas y columnas para extraer los arreglos y mandar a validanoserepite
        #reccoriendo filas y validando
        
        return banderaB
        
    
    #valida que los numero no se repitan dentro de un arreglo de 9 elementos
    def validanoserepite(self,arregloindividual):

        #arregloindividual.sort()
        for i in arregloindividual:
            # si es diferente a 0 entos ingresa para validar cuantas veces existe dentro del arreglo
            if i!=0:
                if arregloindividual.count(i)>1:
                   return False
            #si es 0 no ejecuta codigo
                
        return True