def leerInt(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return int(n)
        else:    
            print('\033[91mError, digite un numero\033[0m')

n = leerInt('Ingrese un numero: ')
print(f'Ingresaste el numero: {n}')
