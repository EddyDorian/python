palabras = ('aprender', 'programar', 'lenguaje', 'python', 'curso')

#mostra las vocales de cada palabra de la tupla
for palabra in palabras:
    print(f'La palabra {palabra.upper()} tiene las vocales: {' '.join([letra for letra in palabra if letra.lower() in 'aeiou'])}')