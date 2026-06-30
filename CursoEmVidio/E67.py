while True:
    numero = int(input('Ingresa un numero: '))
    if numero < 0:
        print('ADIOS')
        break
    for i in range(1, 11):
        print(f'{numero} * {i} = {numero * i}')