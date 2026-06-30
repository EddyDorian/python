from statistics import mean

nota1 = float(input('Primera nota: '))
nota2 = float(input('Segunda nota: '))

media = mean([nota1, nota2])

if media < 5.0:
    mensaje = f'REPROBADO tu nota es: {media}'
elif 5.0 <= media <= 6.9:
    mensaje = f'REFORZAMIENTO tu nota es: {media}'
else:
    mensaje = f'APROBADO tu nota es: {media}'

print(mensaje)