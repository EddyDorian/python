#ejercio anterior
matriz = [[] for _ in range(3)]

pares, tercera = 0, 0
segunda = None

for i in range(3):
    for j in range(3):
        numero = int(input(f'Ingrese un numero para la posicion {i}-{j}: '))
        matriz[i].append(numero)

        if numero % 2 == 0:
            pares += numero

        if j == 2:
            tercera += numero

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]\t', end='')
    print()

print(f'La suma de los pares es: {pares}')
print(f'La suma de la tercera columna es: {tercera}')

segunda = max(matriz[1])
print(f'El mayor valor de 2da fila es: {segunda}')