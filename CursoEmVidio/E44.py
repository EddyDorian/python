from time import sleep

precio = float(input('Ingrese el precio: '))
sleep(1)
print('TIPO DE PAGO')
print('1.- Efectivo / Cheque')
print('2.- Tarjeta')
print('3.- 2x en Tarjeta')
print('4.- 3x en Tarjeta')
tipo = input('Elija una opcion: ')
sleep(1)

if tipo == '1':
    valor = f'{precio - (precio*0.1)}'
elif tipo == '2':
    valor = f'{precio - (precio*0.05)}'
elif tipo == '3':
    valor = f'{precio}'
elif tipo == '4':
    valor = f'{precio + (precio*0.2)}'

print(f'Total a pagar: {valor}')