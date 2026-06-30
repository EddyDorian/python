valor = int(input('Valor a ser sacado: '))
cincuenta = valor // 50
valor %= 50

veinte = valor // 20
valor %= 20

diez = valor // 10
valor %= 10

uno = valor

if cincuenta > 0:
    print(f'50: {cincuenta}')
if veinte > 0:
    print(f'20: {veinte}')
if diez > 0:
    print(f'10: {diez}')
print(f'1: {uno}')