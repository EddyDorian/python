frase = input('Ingrese una expresion matematica: ')
lista = list(frase)

if lista.count('(') == lista.count(')'):
    print('La expresion esta BIEN!!!!')
else:
    print('La expresion esta MAL!!!!')