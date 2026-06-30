import moneda

numero = float(input('Ingrese el precio: '))
print(f'Aumentando el 10% es: {moneda.aumentar(numero, 10)}')
print(f'Disminuyendo el 13% es: {moneda.disminuir(numero, 13)}')
print(f'El doble es: {moneda.doble(numero)}')
print(f'La mitad es : {moneda.mitad(numero)}')