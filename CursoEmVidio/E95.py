registro = []

jugador = {}
goles = []

while True:
    jugador['nombre'] = input('Ingrese el nombre: ')

    for i in range(int(input('Partidos jugados: '))):
        goles.append(int(input(f'Goles en el {i + 1}° partido: ')))

    jugador['goles'] = goles[:]

    jugador['totalGoles'] = sum(goles)

    goles.clear()

    registro.append(jugador.copy())

    respuesta = ' '
    while respuesta not in 'NS':
        respuesta = input('Quieres continuar? [S/N] ').upper().strip()

    if respuesta == 'N':
        break

print('=' * 45)
print(f'{"Cod.":<4} {"Nombre":<10} {"Goles":<20} {"Total":<10}')
print('=' * 45)
for index, jugador in enumerate(registro):
    print(f'{index:<4} {jugador['nombre']:<10} {str(jugador['goles']):<20} {jugador['totalGoles']:<10}')

while True:
    opcion = int(input(f'De que jugador quiere ver los datos: [999 para salir] '))

    if opcion == 999:
        break

    if opcion < 0 or opcion > len (registro):
        print('\nIngrese un Cod. valido')
        continue

    print(f'\nLos datos de {registro[opcion]['nombre']} son:')
    for index, jugador in enumerate(registro):
        if index == opcion:
            for partido, goles in enumerate(jugador['goles']):
                print(f'{"=>":>5} En el {partido + 1}° partido hizo {goles} goles')
            print()

print('Adios!')
