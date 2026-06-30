from random import choice

numeros = [1, 2, 3, 4, 5]

contador = 0

while True:
    jugador = int(input('Ingrese un numero [1 - 5]: '))
    pc = choice(numeros)
    suma = jugador + pc
    eleccion = input('''
        [1] La suma sera par
        [2] La suma sera impar
        :''')
    if eleccion == '1':
        if suma % 2 == 0:
            print(f'Ganaste!!!\n{jugador} + {pc} = {suma}')
            contador += 1
        else:
            print(f'Perdiste!!!\n{jugador} + {pc} = {suma}')
            break
    elif eleccion == '2':
        if suma % 2 != 0:
            print(f'Ganaste!!!\n{jugador} + {pc} = {suma}')
            contador += 1
        else:
            print(f'Perdiste!!!\n{jugador} + {pc} = {suma}')
            break

print(f'Victorias consecutivas: {contador}')