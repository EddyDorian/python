from statistics import mean
nombresF = []
edadesF = []
sexosF = []

nombresM = []
edadesM = []
sexosM = []

for i in range(4):
    nombre = input('Ingrese su nombre: ')
    edad = int(input('Ingrese su edad: '))
    sexo = input('Ingrese su sexo: ')
    print('')

    if sexo == 'masculino':
        nombresM.append(nombre)
        edadesM.append(edad)
        sexosM.append(sexo)
    else:
        nombresF.append(nombre)
        edadesF.append(edad)
        sexosF.append(sexo)

edades = edadesF + edadesM
print(f'El promedio de edad es: {mean(edades)}')

if len(nombresM) > 0:
    posicionMayor = edadesM.index(max(edadesM))
    nombreMayor = nombresM[posicionMayor]
    print(f'El HOMBRE mas mayor es: {nombreMayor}')
else:
    print('No se registraron HOMBRES')

c = 0
for i in range(len(edadesF)):
    if edadesF[i] < 20:
        c += 1
print(f'{c} mujeres menores de 20 anos.')