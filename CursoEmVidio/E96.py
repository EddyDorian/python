def area(largura, comprimento):
    print(f'{'Control de terrenos':^30}')
    print('*' * 30)
    print(f'El area de un terreno de {largura} * {comprimento} es: {largura * comprimento} m2')


area(float(input('Largura: ')), float(input('Comprimento: ')))