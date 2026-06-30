suma, cantidad = 0, 0
menor, mayor = None, None
respuesta = ''

while respuesta in 'Ss':
    numero = int(input('Ingrese un numero: '))
    suma += numero
    cantidad += 1
    if menor is None or numero < menor:
        menor = numero
    elif mayor is None or numero > mayor:
        mayor = numero
    
    respuesta = input('Quieres continuar? (S/N) ')

print(f'La medias es: {suma / cantidad}')
print(f'El mayor es: {mayor}\nEl menor es: {menor}')