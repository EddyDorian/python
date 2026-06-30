from random import choice
c = 1
nombre = ''
lista = []
while c <= 4:
    if nombre:
        lista.append(nombre)
        c += 1
        nombre = ''
    else :
        nombre = input('Ingrese nombre: ')
        
print(f'El elegido es: {choice(lista)}')