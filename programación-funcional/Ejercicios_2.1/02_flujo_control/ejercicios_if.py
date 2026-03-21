from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Determinar el mayor de dos números
print("\nEjercicio 1: Mayor de dos números")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print("El mayor es:", num1)
elif num2 > num1:
    print("El mayor es:", num2)
else:
    print("Los números son iguales")


# Ejercicio 2: Calculadora simple
print("\nEjercicio 2: Calculadora simple")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")


# Ejercicio 3: Año bisiesto
print("\nEjercicio 3: Año bisiesto")

anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")


# Ejercicio 4: Categorizar edades
print("\nEjercicio 4: Categorizar edades")

edad = int(input("Introduce tu edad: "))

if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 3 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")
