ano = int(input('Ingrese un ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('ES Bisiesto')
else: 
    print('No es Bisiesto')