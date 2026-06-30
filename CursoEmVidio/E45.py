#juego de piedra, papel y tijera
from time import sleep
from random import choice

def juzgar(jugador, pc):
    if jugador == pc:
        return f'EMPATE, yo tambien eleji {pc}'
    else:
        if jugador == 'Piedra' and pc == 'Papel':
            return f'PERDISTE, eleji {pc}'
        elif jugador == 'Piedra' and pc == 'Tijera':
            return f'GANASTE, eleji {pc}'
        elif jugador == 'Papel' and pc == 'Piedra':
            return f'GANASTE, eleji {pc}'
        elif jugador == 'Papel' and pc == 'Tijera':
            return f'PERDISTE, eleji {pc}'
        elif jugador == 'Tijera' and pc == 'Piedra':
            return f'PERDISTE, eleji {pc}'
        elif jugador == 'Tijera' and pc == 'Papel':
            return f'GANASTE, eleji {pc}'

opciones = ['Piedra', 'Papel', 'Tijera']

jugador = ''

while jugador != 'Salir':

    print('JUEGO - PIEDRA, PAPEL Y TIJERA')
    print('1.- Piedra')
    print('2.- Papel')
    print('3.- Tijera')
    print('4.- Salir')
    jugador = input('Elija una Opcion: ')
    
    sleep(1)
    
    if jugador != '4':
        jugador = opciones[int(jugador)-1]
        pc = choice(opciones)

        resultado = juzgar(jugador, pc)

        print('\n',resultado,'\n')
    else:
        print('\n','ADIOS','\n')
        jugador = 'Salir'