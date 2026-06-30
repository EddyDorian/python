contador, suma = 0, 0

while True:
    numero = int(input('Ingrese un numero: '))
    if numero == 999:
        break
    contador += 1
    suma += numero

print(f'Se ingresaron: {contador} numeros')
print(f'La suma es: {suma}')