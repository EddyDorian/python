velocidad = float(input('Ingrese la velocidad en Km/h: '))
if velocidad > 80:
    print(f'Fuiste multado\nDebes pagar: {(velocidad - 80) * 7.00}')
else:
    print('No fuiste multado')