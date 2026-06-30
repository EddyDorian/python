total, cantidad, barato = 0, 0, 0
menor = None

while True:
    nombre = input('\nIngrese su nombre: ')
    precio = float(input('Ingrese el precio: '))
    
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quiere continuar? [S/N] ')
    
    total += precio

    if precio > 1000:
        cantidad += 1

    if menor is None or precio < menor:
        menor = precio
        barato = nombre

    if continuar in 'Nn':
        break

print(f'\nTotal: {total}')
print(f'Productos de mas de 1000: {cantidad}')
print(f'Producto mas barato: {barato}')