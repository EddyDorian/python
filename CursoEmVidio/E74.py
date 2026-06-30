from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(numeros)
print(f'El menor es: {min(numeros)}')
print(f'El mayor es: {max(numeros)}')