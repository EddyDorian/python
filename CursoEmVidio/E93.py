jugador = {}
goles = []

jugador['nombre'] = input('Ingrese el nombre: ')

for i in range(int(input('Partidos jugados: '))):
    goles.append(int(input(f'Goles en el {i + 1}° partido: ')))

jugador['goles'] = goles[:]

jugador['totalGoles'] = sum(goles)

print('\n',jugador)
print('=' * 30)
for key, value in jugador.items():
    print(f'{key}: {value}')
print('=' * 30)

print(f'El jugador {jugador['nombre']} jugo {len(jugador['goles'])} partidos')
for index, value in enumerate(jugador['goles']):
    print(f'{"=>":>5} El {1}° partido hizo {value} goles')
print(f'En total hizo {jugador["totalGoles"]} goles')
