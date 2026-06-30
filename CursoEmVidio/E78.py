numeros = []

for i in range(5):
    numero = int(input('Introduzca un numero: '))
    numeros.append(numero)

print(numeros)

mayor = max(numeros)
listaMayores = [str(indice) for indice, valor in enumerate(numeros) if valor == mayor]
menor = min(numeros)
listaMenores = [str(indice) for indice, valor in enumerate(numeros) if valor == menor]

print(f'El mayor es: {mayor} y esta en las posiciones {' '.join(listaMayores)}')    
print(f'El menor es: {menor} y esta en la posicion {' '.join(listaMenores)}')