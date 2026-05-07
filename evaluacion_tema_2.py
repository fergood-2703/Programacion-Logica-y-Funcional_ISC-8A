divisor = "\n----------------------------------------------------"
# ----------------------------------------------------
# EJERCICIO 1: PRESENTACIÓN PERSONAL
# ----------------------------------------------------

nombre = "Omar"
edad = 23   
ciudad = "Felipe Carrillo Puerto"
es_estudiante = True


print("Mi nombre es: " + nombre)
print(f"Mi edad es: {edad}" )
print("Vivo en: " + ciudad)
print(f"¿Soy ISC?: {es_estudiante}")

print(f"Hola, me llamo {nombre}, tengo {edad} años, vivo en {ciudad} y soy ISC")

# Hola, me llamo Carlos, tengo 24 años, vivo en Chetumal y soy ISC.



# ----------------------------------------------------
# EJERCICIO 2: CASA DE CAMBIO
# ----------------------------------------------------
print(divisor)

tasa_cambio = 19.00

usd = input("Ingresa dolares: ")
usd = float(usd)

mxn = usd * tasa_cambio 

print(f"¿Cuántos USD tienes?: {mxn}")

# ----------------------------------------------------
# EJERCICIO 3: ¿QUIEN ES MAYOR DE EDAD?
# ----------------------------------------------------
print(divisor)

print("\nPersona 1: ")
nombre1 = input("Nombre de la primera persona: ")
edad1 = input(f"Edad de {nombre1}: ")
edad1 = float(edad1)


print("\nPersona 2: ")
nombre2 = input("Nombre de la segunda persona:  ")
edad2 = input(f"Edad de {nombre2}: ")
edad2 = float(edad2)

if(edad1>edad2):
    print(f"{nombre1} es mayor que {nombre2} por {edad1 - edad2}")

else:
    print(f"{nombre2} es mayor que {nombre1} por{edad2 - edad1}")
    






