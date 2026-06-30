numero = int(input('Ingrese un nuemro: '))
total = 1

while numero != 1:
    total *= numero
    numero -= 1

print(f'El factorial es: {total}')