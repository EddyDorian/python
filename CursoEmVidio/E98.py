from time import sleep

def contador(inicio, fin, razon):
    
    razon = 1 if razon == 0 else abs(razon)

    print('='* 30)
    print(f'Cuento del {inicio} al {fin}, de {razon} en {razon}')
    if inicio < fin:
        for i in range(inicio, fin + 1, razon):
            print(f'{i}', end = ' ', flush = True)
            sleep(0.5)
    else:
        for i in range(inicio, fin - razon, -razon):
            print(f'{i}', end = ' ', flush = True)
            sleep(0.5)
    print('FIN!')
    

contador(1, 10, 1)

contador(10, 0, -2)

print(f'Conteo Personalizado')
contador(int(input('Inicio: ')), int(input('Fin: ')), int(input('Razon: ')))