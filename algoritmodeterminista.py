"""
Integrantes:
Yesid Fernando Andica - 201556001
Víctor Manuel Marín Duque - 201556071
Stiven Sepulveda Cano - 201556087
"""

""" ============================= Algoritmo determinista ================================ """

import time

#Función para pintar la lista con las coordendas de las reinas
def pintarSolucion(ubicacionReinas):
    print (ubicacionReinas)   
        
#Funcion para comprobar de que en la celda se puede ubicar una reina 
def validarCelda(ubicacionReinas, f, c):
    #Primero se valida si no se encuentra alguna reina en la columna actual
    for i in ubicacionReinas:
        if(c == i):
            return False

    #Se valida que en la diagonal izquierda no se encuentre ninguna reina
    #Para esto se resta 1 en cada iteracion a la coordenada columna y fila en la que 
    #deseamos ubicar la reina
    filaAnterior = f-1
    columnaAnterior = c-1
    for i in range(f):
        #Validamos de que las variables filaAnterior y columnaAnterior no se salgan del tablero
        if(filaAnterior < 0 or columnaAnterior < 0):
          break
        if(ubicacionReinas[filaAnterior] == columnaAnterior):
            return False
        filaAnterior = filaAnterior -1
        columnaAnterior = columnaAnterior-1

    #Se valida que en la diagonal derecha no se encuentre ninguna reina
    #Para esto se resta 1 a la fila y a la columna se suma 1. 
    filaAnterior = f-1
    columnaAnterior = c+1
    for i in range(f):
        #Validamos de que las variables filaAnterior y columnaAnterior no se salgan del tablero
        if(filaAnterior > len(ubicacionReinas) or columnaAnterior < 0):
          break
        if(ubicacionReinas[filaAnterior] == columnaAnterior):
            return False
        filaAnterior = filaAnterior -1
        columnaAnterior = columnaAnterior+1

    return True



def algoritmoDeterminista(ubicacionReinas, f, n):
    """
    Para dar solucion al problema de las n reinas se utiliza la tecnica Backtracking para realizar todas
    las combinaciones posibles.
    ubicacionReinas: es la lista de ubicaciones, hay que tener en cuenta la configuracion de esta lista.
    cada posicion de esta lista hace referencia a una fila en el tablero y el valor que contiene cada posicion
    hace referencia a una columna

    f: es la fila en la que deseamos ubicar la reina

    n: el numero de reinas que se tienen que ubicar en el tabler (el n es igual al tamaño de la lista)
    """
    if f == n:
        return True #Final de la recursión: si el f = n, indica que se llego a una solucion del tablero.

    #Por cada fila, trata de ubicar la reina en las columnas disponibles
    for i in range(n):
        
        #Se valida si la reina puede ubicarse en esa posicion
        if (validarCelda(ubicacionReinas, f, i)):
            ubicacionReinas[f] = i #En la posicion f de la lista se ubica el valor de la columna en la cual
            #fue posicionada la reina

            #Se realiza la recursión hasta que se llegue a un estado final (Se ubiquen todas las reinas).
            if (algoritmoDeterminista(ubicacionReinas, f + 1, n) == True):
                return True

            # Si la reina no puede ubicarse en ninguna celda, se deja el valor por defecto.
            ubicacionReinas[f] = -1
    return False

def solver(n):
    """
    Se utiliza el algoritmoDeterminista para hallar una solucion al tablero dado y se pinta por consola
    las posiciones validas para las reinas.

    Importante: El indice de cada elemento de la lista es la fila donde se debe ubicar la reina
    y el valor de cada indice es la columna.
    """
    ubicacionReinas = []
    for i in range(n):
        #Se inicializa la lista con el valor por defecto -1
        ubicacionReinas.append(-1)
    if(algoritmoDeterminista(ubicacionReinas, 0, n)):
        pintarSolucion(ubicacionReinas)
    else:
        print("Lo siento, no hay solución para este tablero.")

"""valor1 = time.time()
solver(15)
valor2 = time.time()
tiempo_atencion = valor2 - valor1
print(tiempo_atencion)
"""