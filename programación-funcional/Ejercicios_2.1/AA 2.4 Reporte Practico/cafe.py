# Ejercicio 1: Ordenar Cafe para el grupo ISC

'''
1.- Crear una funcion que no tome ningun argumento y devuelva la cadena de texto "cafe".
para simular la preparaci
'''

def preparar_cafe():
    return "cafe"

def odenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe


