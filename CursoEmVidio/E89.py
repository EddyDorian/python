from statistics import mean

registro, persona, notas = [], [], []

while True:
    nombre = input('Ingrese el nombre: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    persona.append(nombre)
    
    notas.append(nota1)
    notas.append(nota2)
    persona.append(notas[:])

    media = mean(notas)
    persona.append(media)

    registro.append(persona[:])

    notas.clear()
    persona.clear()

    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Quiere continuar? [S/N] ').upper().strip()

    if respuesta == 'N':
        break

print(f'{"Nro":<5}{"Nombre":<10}{"Promedio":>5}')
for indice, persona in enumerate(registro):
    print(f'{indice:<5}{persona[0]:<10}{persona[2]:>5}')

respuesta = ' '
while respuesta != '999':
    respuesta = input('Mostrar las nota del alumno: [999 para salir] ')

    if int(respuesta) not in [indice[0] for indice in enumerate(registro)]:
        print('Ingrese el Nro de un estudiante valido')
        continue
    else:
        for indice, estudiante in enumerate(registro):
            if indice == int(respuesta):
                print(f'Las notas de {estudiante[0].upper()} son {estudiante[1]}')

print('ADIOS')