###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

print("\nCrear listas")

lista1 = [1, 2, 3, 4, 5]
lista2 = ["manzanas", "peras", "plátanos"]
lista3 = [1, "hola", 3.14, True]

lista_vacia = []
lista_de_listas = [[1, 2], ["calcetin", 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

print("\nAcceso a elementos por índice")

print(lista2[0])   # manzanas
print(lista2[1])   # peras
print(lista2[-1])  # plátanos
print(lista2[-2])  # peras

print(lista_de_listas[1][0])


print("\nSlicing (rebanado) de listas")

lista1 = [1, 2, 3, 4, 5]

print(lista1[1:4])  # [2, 3, 4]
print(lista1[:3])   # [1, 2, 3]
print(lista1[3:])   # [4, 5]
print(lista1[:])    # [1, 2, 3, 4, 5]

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(lista1[::2])   # pares
print(lista1[::-1])  # invertida

lista1[0] = 20
print(lista1)

lista1 = [1, 2, 3]

lista1 = lista1 + [4, 5, 6]
print(lista1)

lista1 += [7, 8, 9]
print(lista1)

print("Longitud de la lista", len(lista1))