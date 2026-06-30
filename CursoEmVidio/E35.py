uno = float(input('Ingrese una longitud: '))
dos = float(input('Ingrese una longitud: '))
tres = float(input('Ingrese una longitud: '))
if uno + dos > tres and uno + tres > dos and dos + tres > uno:
    print('Pueden formar un Triangulo')
else:
    print('No pueden formar un Triangulo')