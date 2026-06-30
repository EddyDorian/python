from datetime import date

personas = {}

personas['nombre'] = input('Ingrese su nombre: ')
ano = int(input('Ingrese el ano de nacimiento: '))
personas['edad'] = date.today().year - ano
personas['ctp'] = int(input('Ingrese la carteira de trabalho: (0 si no tiene) '))

if personas['ctp'] != 0:
    personas['anoContratacion'] = int(input('Ingrese el ano de contratacion: '))
    personas['salario'] = float(input('Ingrese el salario: '))
    personas['jubilacion'] = (personas["anoContratacion"] - ano) + 35

print('*' * 30)
for key, value in personas.items():
    print(f'{key}: {value}')
print('*' * 30)