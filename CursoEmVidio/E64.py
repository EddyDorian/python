numero, cantidad, suma = 0, 0, 0

while numero != 999:
    numero = int(input('Imgrese un numero: '))
    if numero != 999:
        cantidad += 1
        suma += numero

print(f'Se ingresaron: {cantidad} numeros')
print(f'La suma es: {suma}')