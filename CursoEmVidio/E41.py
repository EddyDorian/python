from datetime import date

ano = int(input('Ano de nacimiento: '))

edad = date.today().year - ano

if edad <= 9:
    print('MIRIM')
elif 9 < edad <= 14:
    print('INFANTIL')
elif 14 < edad <= 19:
    print('JUNIOR')
elif edad == 20:
    print('SENIOR')
else:
    print('MASTER')