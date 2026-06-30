salario = float(input('Ingrese su salario: '))
if salario > 1250.00:
    print(f'Salario: {salario + (salario * 0.10)}')
else:
    print(f'Salario: {salario + (salario * 0.15)}')