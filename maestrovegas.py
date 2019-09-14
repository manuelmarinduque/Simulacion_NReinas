"""
Integrantes:
Yesid Fernando Andica - 201556001
Víctor Manuel Marín Duque - 201556071
Stiven Sepulveda Cano - 201556087
"""

import random
import time

intentos = 0

"""Funcion que ayuda definir hasta que filas intercepta una reina
    en diagonal izquierdo, dada que se encuentra una fila y columna especifica"""
def limitTableroIz(fila, columna,n):
    limitT: int = columna + fila
    if limitT > n:
        return n
    else:
        return limitT

"""Funcion que ayuda definir hasta que filas intercepta una reina
    en diagonal derecho, dada que se encuentra una fila y columna especifica"""
def limitTableroDe(fila, columna,n):
    limitT: int = (n - columna + fila)
    if limitT > n:
        return n
    else:
        return limitT

"""Funcion que se encarga de ver que columnas estan libres
    para que se posicione una reina, de no ser asi retorna un negativo
    simbolizando que no hay espacios en una fila donde se pueda ubicar una reina"""
def funcion1(vb, viz, noz, vde, node, f):

    fila = f
    vectorBase = vb
    vectorIZ = viz
    noIZ = noz
    vectorDe = vde
    noDe = node

    v1 = [i for i, x in enumerate(vectorIZ) if x == fila]
    danger1 = []
    for i in range(0, len(v1)):
        danger1.append(noIZ[v1[i]])

    v2 = [i for i, x in enumerate(vectorDe) if x == fila]
    danger2 = []
    for i in range(0, len(v2)):
        danger2.append(noDe[v2[i]])

    danger=[]
    danger = danger1 + danger2
    aptos = []

    for i in range(0, len(vectorBase)):
        if vectorBase[i] in danger:
            False
        else:
            aptos.append(vectorBase[i])
    if aptos:
        return random.choice(aptos)
    else:
        return -1



"""  Funcion resuelve el problema de las n reinas, recibe una variable "Tamaño" que es
     el que define el tamaño que sera nuestro tablero, si ve que una posicion de una reina
     esta en negativo simboliza que no se puede poner en ninguna columna en una fila dada, 
     lo cual da paso a reiniciar el algoritmo, de lo contrario arma el tablero cumpliendo 
     el criterio de las n reinas"""
def algoritmo(tamaño):

    """ Funcion que ayuda a filtrar las reinas usadas en el tablero para que no haya
        intercepciones en vertical"""
    def filtrar(numero):
        if numero != posicion:
            return True

    global intentos

    accion = True
    fila = 0
    i = 0
    j = 0
    x=tamaño
    y = range(x)

    vectorBase = list(y)
    vectorIZ = []
    noIZ = []

    vectorDe = []
    noDe = []

    tablero = []

    if fila == 0:
        posicion = random.choice(vectorBase)
        vectorBase = (list(filter(filtrar, vectorBase)))
        tablero.append(posicion)
        limiteIz = limitTableroIz(i, posicion, x-1)
        n = posicion
        while (i < limiteIz):
            i = i + 1
            vectorIZ.append(i)
            n = n - 1
            noIZ.append(n)

        limiteDe = limitTableroDe(j, posicion, x-1)
        m = posicion
        while (j < limiteDe):
            j = j + 1
            vectorDe.append(j)
            m = m + 1
            noDe.append(m)

    while fila < x-1:
        fila = fila + 1
        i = fila
        j = fila
        #print("la fila es: ", fila)
        posicion = funcion1(vectorBase,vectorIZ,noIZ,vectorDe,noDe,fila)

        if posicion < 0 :

            accion = False
            break
        else:
            vectorBase = (list(filter(filtrar, vectorBase)))
            tablero.append(posicion)

            limiteIz = limitTableroIz(i, posicion, x-1)

            n = posicion
            while (i < limiteIz):
                i = i + 1
                vectorIZ.append(i)
                n = n - 1
                noIZ.append(n)

            limiteDe = limitTableroDe(j, posicion, x-1)
            m = posicion
            while (j < limiteDe):
                j = j + 1
                vectorDe.append(j)
                m = m + 1
                noDe.append(m)
    if accion == False:
        intentos = 1 + intentos
        return algoritmo(x)

    else:
        intentos = 1 + intentos
        # print("termine ok :)")
        tablero.append(intentos)
        return tablero

def matriz(vector):
    x = vector
    n = len(vector) - 1
    tablero2 = []
    for i in range(0, n):
        valor = x[i]
        filaN = []
        for j in range(0, n):
            if j == valor:
                filaN.append(1)
            else:
                filaN.append(0)
        tablero2.append(filaN)
    return  tablero2

"""valor1 = time.time()
algoritmo(15)
valor2 = time.time()
tiempo_atencion = valor2 - valor1
print(tiempo_atencion)"""