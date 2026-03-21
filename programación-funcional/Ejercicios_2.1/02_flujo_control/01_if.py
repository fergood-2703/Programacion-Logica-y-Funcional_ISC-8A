###
# 01-Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###
from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")
    
    print("\n Sentencia condicional con else")

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
    
    print("\n Sentencia condicional con elif")

nota = 5

if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")
    
    print("\n Condiciones múltiples")

edad = 16
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("POLICIA !!!!!!")
    
    # En un pueblo de Isla Holbox son más relajados

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox")
else:
    print("Paga al policía y te dejará conducir!!!!")
    
    es_fin_de_semana = False

if not es_fin_de_semana:
    print("IISC, anda que hay que ir al Tec!")
    
    print("\n Anidar condicionales")

edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")
    
    numero = 5

if numero:
    print("El número no es cero")

numero = 0

if numero:
    print("Aquí no entrará nunca")
    
    nombre = ""

if nombre:
    print("El nombre no es vacío")
    
    numero = 3  # asignación
es_el_tres = numero == 3  # comparación

if es_el_tres:
    print("El número es 3")
    
    print("\nLa condición ternaria:")

edad = 17

mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
