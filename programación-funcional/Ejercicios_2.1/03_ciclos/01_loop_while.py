###
# 01 - Bucles
#Permiten ejecurar un bloque de codigo repetidamente mientras se cumpla una condición
from os import system
if system("clear") != 0: system("cls")

print("\nBucle while:")

#Bucle con una simple condición
contador = 0
while contador <= 5:
    print(contador)
    contador += 1
    
#Utilizando la palabra break., para romper el bucle
print("\nBucle while con Break: ")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break # se sale del bucle

# continue, que lo hace es saltar esa iteración en concreto y continuar con el bucle
print("\nBucle while con continue: ")
contador = 0
while contador < 10:
    contador += 1
    
    if contador % 2 == 0:
        continue

print(contador)

#else, esta condición cuando se ejecuta?
print("\nBucle while con else: ")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else: 
    print("El bucle a terminado")

#Pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
    numero = int(input("Escribe un número positivo"))
    if numero < 0:
        print("El número debe ser positivo. Intenta otra vez")
        
print(f"El número que has introducido es {numero}")
        
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo. Intenta otra vez")
    except:
        print("Lo que debes introducir es un número!!!")
        
print(f"El numero que has introducido es {numero}")
        
           
 
