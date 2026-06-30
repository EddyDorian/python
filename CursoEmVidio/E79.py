numeros = []

while True:
    numero = int(input('Ingrese un numero: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Agregado correctamente.')
    else:
        print('El numero No se agrego, ya que ya esta presente en la lista')

    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Queire continuar? [S/N] ').upper().strip()[:1]

    if respuesta == 'N':
        break

print(f'\n{sorted(numeros)}')