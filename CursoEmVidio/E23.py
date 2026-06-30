numero = 'a'
while numero != '':
    if numero.isnumeric():
        numero = numero.rjust(4, '0')
        print('Forma de cadena')
        print(f'unidades: {numero[3]}')
        print(f'decenas: {numero[2]}')
        print(f'centenas: {numero[1]}')
        print(f'miles: {numero[0]}')

        print('Forma Numerica')
        numero = int(numero)
        print(f'unidades: {numero % 10}')
        print(f'decenas: {(numero // 10) % 10}')
        print(f'centenas: {(numero // 100) % 10}')
        print(f'miles: {(numero // 1000) % 10}')
        break
    else:
        numero = input('Ingrese un numero: ')