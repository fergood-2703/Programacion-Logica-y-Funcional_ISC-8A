#Ejercicio 2
#objetivo : Ordenar distintos tipos de café 

"""Los grupos de VIII de ISC tienne cambios de humor y ahora cada grupo quiere un tipo de café
--cafe americano
--cafe americano

***Dato curioso: Los cambios de humor de mis alumnos son bastantes frecuentes

con esta informacion, dtendremos que revisar el funcion orndenar 


1.-
"""
def cafe_americano():
    return "café americano"

def cafe_olla():
    return "café de olla"

def ordenar_cafe (tipo_cafe, num_tazas):
    tazas_cafe = [tipo_cafe() for _ in range(num_tazas)]
    return tazas_cafe

grupo_A = ordenar_cafe(cafe_americano,10)
grupo_B = ordenar_cafe(cafe_olla,12)

print (grupo_A, grupo_B)

