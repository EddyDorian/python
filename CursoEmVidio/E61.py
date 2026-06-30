primero = int(input('Ingrese el primer termino: '))
razon = int(input('Ingrese la razon: '))

c = 1
pa = ''

while c != 11:
    pa += f'{primero} -> '
    primero += razon
    c += 1

print(f'{pa} FIN')