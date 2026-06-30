from random import randint
from time import sleep

jugadas = {
    'uno': randint(1,6),
    'dos': randint(1,6),
    'tres': randint(1,6),
    'cuatro': randint(1,6)
}
for key, value in jugadas.items():
    print(f'El jugador {key}, obtuvo el numero {value}')
    sleep(1)

print('RANKING')    
resultado = sorted(jugadas.items(), key=lambda x: x[1], reverse=True)

for index, jugador in enumerate(resultado):
    print(f'{index + 1} lugar: {jugador[0]} con {jugador[1]}')
    sleep(1)