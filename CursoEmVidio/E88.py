from random import sample
from time import sleep

juegos = []

nJuegos = int(input('Cuantos juegos quieres?: '))

juegos = [[] for _ in range(nJuegos)]

for i in range(len(juegos)):
    for _ in range(6):
        juegos[i] = sample(range(1, 60), 6)[:]

for posicion, palpitos in enumerate(juegos):
    print(f'El juego numero {posicion + 1} es: {palpitos}')
    sleep(1)
