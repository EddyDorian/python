from time import sleep
numero = int(input('Introduzca un numero: '))
print('bases de conversion'.capitalize())
print('1.- binario'.capitalize())
print('2.- octal'.capitalize())
print('3.- hexadecimal'.capitalize())
opcion = input('Elija una opcion: ')
sleep(1)
if opcion == '1':
    print(f'Binario: {bin(numero)[2:]}')
elif opcion == '2':
    print(f'Octal: {oct(numero)[2:]}')
elif opcion == '3':
    print(f'Hexadecimal: {hex(numero)[2:]}')
else:
    print('Opcion no valida')