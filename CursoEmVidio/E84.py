registros, persona = [], []

mayor, menor = None, None

while True:
    persona.append(input('Ingrese su nombre: '))
    persona.append(float(input('Ingrese su peso: ')))
    registros.append(persona[:])

    persona.clear()

    respuesta = ' '
    while respuesta not in 'SN':
        respuesta = input('Quiere continuar? [S/N] ').upper().strip()

    if respuesta == 'N':
        break

print(f'Personas registradas: {len(registros)}')

mayor = max(registros, key=lambda x : x[1])[1]
menor = min(registros, key=lambda x : x[1])[1]
pesadas = [persona[0] for persona in registros if persona[1] == mayor]
livianas = [persona[0] for persona in registros if persona[1] == menor]

print(f'El mayor peso es: {mayor} Kg y las personas son: {pesadas}')
print(f'El menor peso es: {menor} Kg y las personas son: {livianas}')