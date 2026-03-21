###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("Fernando")
print("Felipe Carrillo Puerto")

print("-------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("-------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
num = "12345"
num_int = int(num)
num_float = float(num_int)
print(num_int)
print(num_float)

decimal = 3.99
entero = int(decimal)
print(entero)  # Se rompe, no funciona

print("-------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# ¡Hola! Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

### Completa aquí
nombre = "Fernando"
edad = 22
altura = 1.59

print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {altura} metros")

print("-------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.1416
redondeado = round(pi)
resultado = redondeado // 2

print(redondeado)
print(resultado)