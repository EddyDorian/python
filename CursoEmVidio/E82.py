numeros = []

pares, impares = [], []

while True:
    numero = int(input('Ingrese un numero: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Quiere continuar? [S/N] ').strip().upper()
    
    if respuesta == 'N':
        break

print(f'La lista original es: {numeros}')
print(f'La lista de pares es: {pares}')
print(f'La lista de impares es: {impares}')