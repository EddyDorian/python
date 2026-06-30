numero = int(input('Ingrese un numero primo: '))

c = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        c += 1

if c <= 2:
    print(f'El {numero} es PRIMO')
else:
    print(f'El {numero} NO ES PRIMO')