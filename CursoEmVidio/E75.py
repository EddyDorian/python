uno = int(input('Ingrese un numero: '))
dos = int(input('Ingrese un numero: '))
tres = int(input('Ingrese un numero: '))
cuatro = int(input('Ingrese un numero: '))
    
numeros = (uno, dos, tres, cuatro)

pares = ''

for indice, valor in enumerate(numeros):
    if valor % 2 == 0:
        pares += f'{valor}, '

print(f'El 9 aparecio: {numeros.count(9)} veces')

if numeros.count(3) > 0:
    print(f'El 3 aparecio por primera vez en la posicion: {numeros.index(3) + 1}')

print(f'Los pares son: {pares[:-2]}')