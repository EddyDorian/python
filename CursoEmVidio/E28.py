from random import randint
from time import sleep
print('Pensando un numero......')
sleep(1)
numero = randint(0, 5)
intento = int(input('Intenta adivinar el numero que elegi: '))
if intento == numero:
    print('Correcto')
else:
    print(f'Fallaste, elegi el numero: {numero}')