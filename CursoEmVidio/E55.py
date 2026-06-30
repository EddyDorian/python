#pesos = []

#for i in range (5):
#    peso = float(input('Ingrese su peso: '))
#    pesos.append(peso)

#print(f'Mayor: {max(pesos)}')
#print(f'Menor: {min(pesos)}')


mayor = 0 
menor = 999999999999

for i in range (5):
    peso = float(input('Ingrese su peso: '))
    if peso > mayor:
        mayor = peso
    elif peso < menor:
        menor = peso

print(f'Mayor: {mayor}')
print(f'Menor: {menor}')