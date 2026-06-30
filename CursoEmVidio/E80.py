numeros = []

for i in range(5):
    numero = int(input('Ingrese un numero: '))
    if i == 0:
        numeros.append(numero)
        print(f'Agregado en la posicion 0 de la lista')
    elif i == 1:
        if numero < numeros[0]:
            numeros.insert(0, numero)
            print(f'Agregado en la posicion 0 de la lista')
        else:
            numeros.append(numero)
            print(f'Agregado en la posicion {i} de la lista')
    elif i >= 2:
        for j in range(len(numeros)):
            if numero < numeros[j]:
                numeros.insert(j, numero)
                print(f'Agregado en la posicion {j} de la lista')
                break
            if j == len(numeros) - 1:
                numeros.append(numero)
                print(f'Agregado en la posicion {len(numeros) - 1} de la lista')
                
print(numeros)