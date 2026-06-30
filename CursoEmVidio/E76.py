productos = ('Lapis', 1.75, 'Goma', 2, 'cuaderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compas', 9.99, 'mochila', 120.32, 'boligrafos', 22.30, 'Libro', 34.90)

print('-'*30)
print('LISTA DE PRECIOS'.center(30, ' '))
print('-' *30)
for i in range(0, len(productos), 2):
    item = f'{productos[i]:.<20}Bs{productos[i + 1]:>8.2f}'
    print(item)
print(f'-'*30)