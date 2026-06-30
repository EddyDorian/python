import moneda

numero = float(input('Ingrese el precio: '))
print(f'\nAumentando el 10% es: {moneda.moneda(moneda.aumentar(numero, 10))}')
print(f'Disminuyendo el 13% es: {moneda.moneda(moneda.disminuir(numero, 13))}')
print(f'El doble de {moneda.moneda(numero)} es: {moneda.moneda(moneda.doble(numero))}')
print(f'La mitad de {moneda.moneda(numero)} es : {moneda.moneda(moneda.mitad(numero))}')