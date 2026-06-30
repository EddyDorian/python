peso = float(input('Peso: '))
altura = float(input('Altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    estado = f'Bajo de peso'
elif 18.5 <= IMC < 25:
    estado = f'Peso ideal'
elif 25 <= IMC < 30:
    estado = 'Sobrepeso'
elif 30 <= IMC < 40:
    estado = 'Obesidad'
else:
    estado = 'Obesidad morbida'

print(estado)