numeros = [[] for _ in range(2)]

for i in range(7):
    numero = int(input('Ingrese un numero: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(sorted(numeros[0]))
print(sorted(numeros[1]))