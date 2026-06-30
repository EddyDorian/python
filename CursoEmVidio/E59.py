from time import sleep

opcion = ''

uno = dos = 0

uno = float(input('Ingresa el primer numero: '))
dos = float(input('Ingresa el segundo numero: '))

while opcion != '5':
    print('''
        MENU
        [1] Sumar
        [2] Multiplicacion
        [3] Mayor
        [4] Nuevos Numeros
        [5] Salir del programa
    ''')
    
    opcion = input('Que deceas hacer? ')

    if opcion == '1':
        print(f'\n{uno} + {dos} = {uno + dos}\n')
        sleep(2)
    elif opcion == '2':
        print(f'\n{uno} * {dos} = {uno * dos}\n')
        sleep(2)
    elif opcion == '3':
        if uno > dos:
            print(f'\nEl mayor es: {uno}\n')
        else:
            print(f'\nEl mayor es: {dos}\n')
        sleep(2)
    elif opcion == '4':
        uno = float(input('Ingresa el primer numero: '))
        dos = float(input('Ingresa el segundo numero: '))
        sleep(1)
    elif opcion == '5':
       print('\nADIOS\n') 
       sleep(2)
    else:
       print('\nIngresa una opcion valida\n') 
       sleep(2)