n = int(input('Ingrese un numero: '))

c = 2

primero = 0
segundo = 1

fibonacci = f'{primero} -> {segundo} -> '

if n == 0:
    print('Ingrese un numero valido')
elif n == 1:
    print(primero)
elif n == 2:
    print(fibonacci[:-4])
else:
    while c < n:
        nuevo = primero + segundo
        fibonacci += f'{nuevo} -> '
        primero = segundo
        segundo = nuevo
        c += 1

    print(f'{fibonacci[:-4]}')