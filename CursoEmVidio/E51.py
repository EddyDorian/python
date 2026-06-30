primro = int(input('Ingrese el primer termino: '))
razon = int(input('Ingrese la razon: '))

progresion = ''

for i in range(1, 11):
    progresion += f'{primro} -> '
    primro += + razon
progresion += 'FIN'

print(progresion)