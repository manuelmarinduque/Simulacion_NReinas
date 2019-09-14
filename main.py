import simpy
import simulacion
import numpy as np

# Inicio de la simulación:
print('Negocio de arepas')
# random.seed(SEMILLA)
env = simpy.Environment()
servidor = simpy.Resource(env, capacity=1)
robot = simulacion.Cliente(env, servidor)
env.process(simulacion.finalizacion(env, robot))
env.run()

# Visualización de las variables de desempeño:
print(f"Cola máxima {simulacion.MAX_COLA}")
print(f'El tiempo promedio de espera es: {np.mean(simulacion.ESPERA_ROBOT):7.2f}')
print(f'La utilidad propia de la persona es {simulacion.UTILIDAD}')
print(f'La utilidad del profesor es {simulacion.UTILIDAD_PROFESOR}')
print(f'El profesor perdió una cantidad de {simulacion.PIERDE_PROFESOR} veces')
