import moneda

numero = float(input('Ingrese el precio: '))
print(f'\nAumentando el 10% es: {moneda.aumentar(numero, 10, True)}')
print(f'Disminuyendo el 13% es: {moneda.disminuir(numero, 13, True)}')
print(f'El doble de {moneda.moneda(numero)} es: {moneda.doble(numero, True)}')
print(f'La mitad de {moneda.moneda(numero)} es : {moneda.mitad(numero, True)}')