from random import sample, randint
from time import sleep

def sortea():
    return sample(range(1, 11), 5)

def sumaPar(lista):
    print(f'Se sortearon los numeros:', end=' ')
    for i in numeros:
        print(i, end=' ', flush=True)
        sleep(0.5)

    print(f'\nLa suma de los pares es: {sum([numero for numero in lista if numero % 2 == 0])}')

numeros = []


numeros = sortea()
sumaPar(numeros)