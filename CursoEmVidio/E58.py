from random import randint
from time import sleep

numero = ''

numeroPc = randint(0, 10)
c = 0

print('ADIVINA EL NUMERO EN EL QUE ESTOY PENSANDO')
sleep(1)
print('Estoy pensando en numero entre el 0 y el 10')
sleep(1)

while numero != numeroPc:
    numero = int(input('Intenta adivinar el numero que estoy pensando: '))
    c += 1

print(f'Acertates, estaba pensando en el numero {numeroPc}')
print(f'Necesitaste: {c} intentos')