frase = input('Ingrese una frase: ').strip()
print(f'A: {frase.lower().count('a')}')
print(f'primero: {frase.lower().find('a')+1}')
print(f'ultimo: {frase.lower().rfind('a')+1}')