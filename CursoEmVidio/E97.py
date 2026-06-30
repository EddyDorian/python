def escribir(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))

escribir('Hola mundo!')

escribir('Eddy Dorian Rojas Medina')