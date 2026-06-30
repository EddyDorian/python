alumnos = {}

alumnos['nombre'] = input('Ingrese el nombre: ')
alumnos['media'] = float(input(f'Ingrese el promedio de {alumnos['nombre']}: '))
if alumnos['media'] < 5:
    alumnos['situacion'] = 'Reprobado'
elif 5 <= alumnos['media'] < 7:
    alumnos['situacion'] = 'Recuperacion'
elif alumnos['media'] >= 7:
    alumnos['situacion'] = 'Aprobado'

print()
for key, value in alumnos.items():
    print(f'El {key} es: {value}')