from datetime import date

ano = int(input('Ano de nacimiento: '))

if date.today().year - ano < 18:
    print(f'Te tienes que enlistar en {18 - (date.today().year - ano)} anos')
elif (date.today().year - ano) > 18:
    print(f'Ya te enlistaste hace {(date.today().year - ano) - 18} anos')
else:
    print(f'Enlistate ahora')