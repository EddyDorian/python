numeros = ('cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte')

while True:
    numero = int(input('Ingrese un numero entre 0 y 20: '))
    if 0 <= numero <= 20:
        break

print(f'{numeros[numero]}')