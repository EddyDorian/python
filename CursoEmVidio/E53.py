frase = input('Ingrese una frase: ')
#volteada = ''.join(reversed(frase.replace(' ', '')))

#if frase.lower().replace(' ', '') == volteada.lower():
#    print('SON PALINDROMAS')
#else:
#    print('NO SON PALINDROMAS')

volteada = ''

frase = frase.replace(' ', '')

for i in range(len(frase) - 1, -1, -1):
    volteada += frase[i]

if frase.lower() == volteada.lower():
    print('SON PALINDROMOS')
else:
    print('NO SON PALINDROMOS')