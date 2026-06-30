from datetime import date
mayores = menores = 0

for i in range(7):
    ano = int(input('Ingrese el ano: '))
    if date.today().year - ano > 21:
        mayores += 1
    else:
        menores += 1

print(f'{mayores} Mayores\n{menores} Menores')