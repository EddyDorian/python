def linea():
    print('~'*28)

def titulo(txt):
    linea()
    print(txt.center(28))
    linea()

def leerNumero(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('Debe ingresar un \033[91mNUMERO ENTERO\033[0m')
        except KeyboardInterrupt:
            print('\n\033[91mSe interrumpio la ejecucion del programa\033[0m')
            return 3
        else:
            return n

def menu(*args):
    while True:
        titulo('MENU')
        for index, value in enumerate(args):
            print(f'\033[93m{index+1:>5} \033[94m{value:<20}\033[0m')
        n = leerNumero('\033[92mQue decea hacer?\033[0m ')
        return n