from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: El mensaje secreto
print("\nEjercicio 1: El mensaje secreto")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = "".join(mensaje)

print("El mensaje secreto es:", mensaje_secreto)


# Ejercicio 2: Intercambio de posiciones
print("\nEjercicio 2: Intercambio de posiciones")

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]

print("Lista con posiciones intercambiadas:", numeros)


# Ejercicio 3: El sándwich de listas
print("\nEjercicio 3: El sándwich de listas")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print("Sandwich:", sandwich)


# Ejercicio 4: Duplicando la lista
print("\nEjercicio 4: Duplicando la lista")

lista = [1, 2, 3]
lista_duplicada = lista * 2

print("Lista duplicada:", lista_duplicada)


# Ejercicio 5: Extrayendo el centro
print("\nEjercicio 5: Extrayendo el centro")

lista = [10, 20, 30, 40, 50]
centro = lista[len(lista)//2]

print("El elemento del centro es:", centro)


# Ejercicio 6: Reversa parcial
print("\nEjercicio 6: Reversa parcial")

lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2

resultado = lista[:mitad][::-1] + lista[mitad:]

print("Resultado:", resultado)
