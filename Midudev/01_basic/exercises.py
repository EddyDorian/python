###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre, ciudad = input('Introuzca su Nombre y Ciudad (Separados por ","):\n').split(',')
print(f'Nombre: {nombre.strip().title()}\nCiudad: {ciudad.strip().title()}')

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f'{a:<12} -> {type(a)}')
print(f'{b:<12} -> {type(b)}')
print(f'{c:<12} -> {type(c)}')
print(f'{d:<12} -> {type(d)}')
print(f'{str(e):<12} -> {type(e)}')

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
numero = "12345"
print(f'Numero: {numero:<8} -> {type(numero)}')
print(f'Numero: {int(numero):<8} -> {type(int(numero))}')
print(f'Numero: {float(numero):<8} -> {type(float(numero))}')
print()
numero = 3.99
print(f'Numero: {numero:<8} -> {type(numero)}')
print(f'Numero: {int(numero):<8} -> {type(int(numero))}')
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre, edad, altura = input('Ingrese su Nombre, Edad y Altura (Separados por ","):\n').split(',')
print(f'Hola! Me llamo {nombre.strip().title()} y tengo {edad.strip()} años, mido {altura.strip()} metros')

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
print(f'PI (aproximado) = {3.14159}')
print(f'Redondeado: {round(3.14159)}')
print(f'Division Entera: {round(3.14159)} // 2 = {round(3.14159) // 2}')