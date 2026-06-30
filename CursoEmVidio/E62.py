n = 1
tope = 10
aumento = 0

c = 1
pa = ''

primero = int(input('Ingrese el primer termino: '))
razon = int(input('Ingrese la razon: '))

while True and aumento != -1:
    if c <= tope:
        pa += f'{primero} -> '
        primero += razon
        c += 1
    else:
        print(f'{pa[:-4]}')
        aumento = int(input('Cuantos terminos mas quieres ver? '))
        if aumento != 0:
            tope += aumento
        else:
            aumento = -1    

print(f'{pa} FIN')