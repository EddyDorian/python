valor = float(input('Valor de la casa: '))
salario = float(input('Salario: '))
anos = float(input('Anos a pagar: '))

if (valor / (anos* 12)) <= (salario*0.30):
    print(f'Prestacion: {valor / (anos * 12)}')
else:
    print('Prestamo negado')