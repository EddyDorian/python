uno = float(input('Ingrese un lado: '))
dos = float(input('Ingrese un lado: '))
tres = float(input('Ingrese un lado: '))

if uno + dos > tres and dos + tres > uno and uno + tres > dos:
    if uno == dos == tres:
        print('Forman un Triangulo EQUILATERO')
    elif uno == dos or uno == tres or dos == tres:
        print('Forman un triangulo ISOSELES')
    else:
        print('Forman un triangulo ESCALENO')
else:
    print('NO pueden formar un TRIANGULO')