matriz = [[] for _ in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i].append(input(f'Ingrese un valor para la posicion {i}-{j}: '))

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]\t', end='')
    print()
