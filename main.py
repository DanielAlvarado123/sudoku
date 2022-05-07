#unificar pygame con logica de sudoky y frontend
#importando las clases
import logicasudoku
import frontedSudoku

#inicializando las clases
logica = logicasudoku.cuerpo()
interfaz = frontedSudoku.imagenessudoku(2,2)
  
#Generando el cuerpo del sudoku
logica.creandoCuerpo()
#obteniendo el cuerdo del sudoku
tempralcuerpo= logica.cuerposudoku
#recorriendo el cuerpo que se asigno en la variable tempralcuerpo

logica.dificultad()
