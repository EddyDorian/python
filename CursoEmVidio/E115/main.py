from lib.vistas import *
from lib.archivos import *
from time import sleep

file = 'dato.txt'
while True:
    eleccion = menu('Registrar', 'Listar', 'Salir')

    if eleccion == 1:
        linea()
        nombre = input('Nombre: ').strip().capitalize()
        edad = leerNumero('Edad: ')
        registrar(file, nombre, edad)
        sleep(2)
    elif eleccion == 2:
        mostrar(file)
        sleep(2)
    elif eleccion == 3:
        print('ADIOS!')
        break
    else:
        print('Elija una opcion valida')