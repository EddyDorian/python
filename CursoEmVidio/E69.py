mayores, hombres, mujeres = 0, 0, 0
sexo = ''

while True:
    edad = int(input('\nIngrese su edad: '))

    sexo = input('Ingrese su Sexo [M/F]: ')
    while sexo not in 'FfMm':
        sexo = input('Ingrese su Sexo [M/F]: ')

    if edad > 18:
        mayores += 1
    if sexo in 'Mm':
        hombres += 1
    if edad < 20 and sexo in 'Ff':
        mujeres += 1
    
    continuar = input('Continuar? [S/N]: ')
    if continuar in 'Ss':
        continue
    if continuar not in 'SsNn':
        while continuar not in 'SsNn':
            continuar = input('Continuar? [S/N]: ')
    if continuar in 'Nn':
        break

print(f'\nPersonas mayores de 18 anos: {mayores}')
print(f'Hombres registrados: {hombres}')
print(f'Mujeres menores de 20 anos: {mujeres}')