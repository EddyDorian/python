def ficha(nombre='<desconocido>', goles='0'):
    print(f'El jugador {nombre}, hizo {goles} goles en el campeonato.')

nombre = input('Nombre del jugador: ')
goles = input('Goles marcados: ')
if not nombre and not goles:
    ficha()
elif not nombre.strip():
    ficha(goles = goles)
elif not goles or not  goles.isnumeric():
    ficha(nombre = nombre)
else:
    ficha(nombre, goles)