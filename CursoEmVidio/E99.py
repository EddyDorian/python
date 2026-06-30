from time import sleep

def maior(*numeros):
    if not numeros:
        print('No se pasaron numeros por tanto', end = '') 
    else:
        print(f'Se analizaron {len(numeros)} numeros: ', end=' ')
        for i in numeros:
            print(f'{i}', end = ' ', flush = True)
            sleep(0.5)

    print(f', El mayor es: {max(numeros) if len(numeros) > 0 else 0}')
    print('*' * 50)

maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()