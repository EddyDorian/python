from statistics import mean

registros = []

persona = {}

while True:
    persona['nombre'] = input('Ingrese el nombre: ')

    persona['sexo'] = '  '
    while persona['sexo'] not in 'MF':
        persona['sexo'] = input('Ingrese el sexo: [M/F] ').upper().strip()

    persona['edad'] = int(input('Ingrese la edad: '))

    registros.append(persona.copy())

    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Quiere continuar? [S/N] ').upper().strip()

    if respuesta == 'N':
        break

print(registros)
    
print(f'\nSe registraron {len(registros)} personas')

media = mean([persona['edad'] for persona in registros])
print(f'\nLa media de edad es {media:.2f}')

print(f'\nLas mujeres registradas son:')
for persona in registros:
    if persona['sexo'] == 'F':
        print(f'{"=>":>5} Nombre: {persona['nombre']}, Edad: {persona['edad']}')

print(f'\nLas personas con edad por encima de la media son:')
for persona in registros:
    if persona['edad'] > media:
        print(f'{"=>":>5} Nombre: {persona['nombre']}, Sexo: {persona['sexo']}, Edad: {persona['edad']}')

