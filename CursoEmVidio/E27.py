nombre = input('Ingrese su nombre: ').strip()
print(f'primero: {nombre.split()[0]}')
lista = nombre.split()
print(f'ultimo: {nombre.split()[len(lista) - 1]}')