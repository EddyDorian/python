from random import shuffle
c = 1
nombre = ''
lista = []
while c <= 4:
    if nombre:
        lista.append(nombre)
        c += 1
        nombre =''
    else:
        nombre = input('Ingrese el nombre: ')
shuffle(lista)
print(lista)