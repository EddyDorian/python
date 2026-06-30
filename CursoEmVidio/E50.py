suma = 0
for i in range(1, 7):
    numero = int(input('Ingrese un numero: '))
    if numero % 2 == 0:
        suma += numero
print(f'La suma de los pares es: {suma}')