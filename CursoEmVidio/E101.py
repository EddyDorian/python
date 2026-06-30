from datetime import date

def voto(nacimento):
    
    if (date.today().year - nacimento) < 16:
        return 'Negado'
    
    elif 16 <= (date.today().year - nacimento) <= 18 or (date.today().year - nacimento) > 65:
        return 'Opcional'

    else:
        return 'Obligatorio'

nacimiento = int(input('Ano de Nacimiento: '))
print(f'Con {date.today().year - nacimiento}, el voto es: {voto(nacimiento)}')
