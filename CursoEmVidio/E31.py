distancia = float(input('Ingrese la distancia en Km: '))
if distancia > 200:
    print(f'Pasaje: {distancia * 0.45}')
else:
    print(f'Pasaje: {distancia * 0.50}')