# -*- coding: utf-8 -*-

"""
Integrantes:
Victor Manuel Marín Duque - 201556071
Yesid Fernando Andica - 201556001
Stiven Sepulveda Cano - 201556087
"""

import random
import simpy
import numpy as np
import maestrovegas as vegas
import algoritmodeterminista as determinista
import time

# Datos de la simulación
TIEMPO_TRABAJO = 480

# Variables desempeño
COLA = 0
MAX_COLA = 0
ESPERA_ROBOT = np.array([])
UTILIDAD_PROFESOR = 0
UTILIDAD = 0
PIERDE_PROFESOR = 0

# Función que provoca una interrupción (excepción) en el proceso 'llegada' 
# cuando el tiempo simulado alcance 480 UT (Unidades de tiempo, en minutos):
def finalizacion(env, robot):
    yield env.timeout(TIEMPO_TRABAJO)
    robot.action.interrupt()

class Cliente():

	# Constructor de la clase:
	def __init__(self, env, servidor):
		self.__env = env
		self.__mesero = servidor
		# Comienza el proceso 'llegada' cuando se crea una instancia de 'Cliente':
		self.action = env.process(self.__llegada())

	def __llegada(self):
		try:
			# Se generan 1000 robots; dado que los eventos de llegada terminan al pasar 480 UT,
			# tal cantidad de robots realmente no llegan al negocio:
			for i in range(1000):
				# Comienza el proceso 'salida':
				self.__env.process(self.__salida(f'{i}'))
				# Llegada de los robots con una distribución uniforme entre 10 y 30 minutos:
				tiempo_llegada = random.uniform(10,30)
				# El proceso 'llegada' se queda esperando hasta que se active el evento Timeout al 
				# pasar el tiempo indicado por el valor de 'tiempo_llegada'. Esto genera la llegada
				# del siguiente robot:
				yield self.__env.timeout(tiempo_llegada)
		# Se captura la excepción de interrupción para que no lleguen más robots:
		except simpy.Interrupt:
			print('Ya no se reciben mas robots')    
            
	def __salida(self, nombre):
    	# El robot llega y se va cuando se le atiende o acaba el juego:
		llegada = self.__env.now
		print(f'Al minuto{self.__env.now:7.2f} llega el robot {nombre}')

		# Variables globales:
		global COLA
		global MAX_COLA
		global ESPERA_ROBOT
		global UTILIDAD
		global UTILIDAD_PROFESOR
		global PIERDE_PROFESOR

    	#Atendemos a los robots (retorno del yield)
    	# El robot ocupa al mesero:
		with self.__mesero.request() as req:

			# Se aumenta el tamaño de la cola al llegar un robot:
			COLA += 1
			if COLA > MAX_COLA:
				MAX_COLA = COLA
			
			print(f'Tamaño de la cola: {COLA}')

			# Si el profesor está ocupado jugando con otro robot, el robot actual espera
			# a que se desocupe y sea atendido:
			yield req
			# Una vez desocupado el profesor y empiece a atender el robot en cola, se disminuye la cola:
			COLA = COLA - 1
			# Se calcula el tiempo que esperó el robot:
			espera = self.__env.now - llegada
			# El tiempo de espera se añade a una lista para poder calcular el tiempo promedio de espera:
			ESPERA_ROBOT = np.append(ESPERA_ROBOT, espera)
			print(f'Al minuto{self.__env.now:7.2f} el robot {nombre} es atendido, esperando{espera:7.2f} minutos en cola')

			# Se selecciona un n para el tamaño del tablero
			n_tablero = random.choice([4,5,6,8,10,12,15])
			print(f'Tamaño del tablero {n_tablero}')

			# Se calcula el tiempo de ejecución del algoritmo Las Vegas:
			valor1 = time.time()
			vegas.algoritmo(n_tablero)
			valor2 = time.time()
			tiempo_vegas = valor2 - valor1
			print(f'Las vegas demoró {tiempo_vegas}')

			# Se calcula el tiempo de ejecución del algoritmo deterministico:
			valor3 = time.time()
			determinista.solver(n_tablero)
			valor4 = time.time()
			tiempo_determinista = valor4 - valor3
			print(f'Determinista demoró {tiempo_determinista}')

			# El menor tiempo de ejecución indica quién ganó el juego:
			if tiempo_vegas < tiempo_determinista:
				print("			Gana el robot")
				UTILIDAD -= 10
				PIERDE_PROFESOR += 1
				# Se realiza el tiempo de servicio:
				yield self.__env.timeout(tiempo_vegas*10000)
			else:
				print("			Gana el profesor")
				UTILIDAD += 15
				UTILIDAD_PROFESOR += 15
				# Se realiza el tiempo de servicio:
				yield self.__env.timeout(tiempo_determinista*10000)
			
			print(f'Al minuto{self.__env.now:7.2f} sale el robot {nombre}')


# Inicio de la simulación

print('Negocio de arepas')
env = simpy.Environment()
servidor = simpy.Resource(env, capacity=1)
robot = Cliente(env, servidor)
env.process(finalizacion(env, robot))
env.run()

print(f"Cola máxima {MAX_COLA}")
print(f'El tiempo promedio de espera es: {np.mean(ESPERA_ROBOT):7.2f}')
print(f'La utilidad propia de la persona es {UTILIDAD}')
print(f'La utilidad del profesor es {UTILIDAD_PROFESOR}')
print(f'El profesor perdió una cantidad de {PIERDE_PROFESOR} veces')
