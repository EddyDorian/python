from lib.vistas import *

def registrar(archivo, nombre, edad):
    registro = f'{nombre};{edad}\n'
    with open(archivo, 'a') as file:
        file.write(registro)
        
    print()
    print('Se registro exitosamente!')
    print()

def mostrar(archivo):
    titulo('REGISTROS')
    with open(archivo, 'r') as file:
        for linea in file:
            datos = linea.split(';')
            print(f'{datos[0]:<25}{datos[1].replace('\n', ''):<10}')

    print()