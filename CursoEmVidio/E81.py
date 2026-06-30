numeros = []
cantidad = 0

while True:
    numeros.append(int(input('Ingrese un numero: ')))
    cantidad += 1
    
    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Quiere continuar? [S/N] ').strip().upper()
    
    if respuesta == 'N':
        break

print(f'Se introdujeron {cantidad} numeros')

numeros.sort(reverse=True)
print(f'Lista decreciente: {numeros}')

print(f'{"El 5 SI esta!" if 5 in numeros else "El 5 NO esta!"}')