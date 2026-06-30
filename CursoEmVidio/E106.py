from time import sleep

def titulo(txt, sub = False):
    tamano = len(txt) + 4

    if sub:
        print(f'\033[41m~\033[0m' * (tamano))
        print(f'\033[41m{txt:^{tamano}}\033[0m')
        print(f'\033[41m~\033[0m' * (tamano))
    else:
        print(f'\033[44m\033[97m~\033[0m' * (tamano))
        print(f'\033[44m\033[97m{txt:^{tamano}}\033[0m')
        print(f'\033[44m\033[97m~\033[0m' * (tamano))


def ayuda():
    while True:
        titulo('SISTEMA DE AYUDA')
    
        funcion = input(f'\033[96mNombre de la funcion/comando [FIN para salir]>\033[0m ').strip().lower()

        if funcion.upper() == 'FIN':
            break

        titulo(f'Accesando al manual del comando {funcion.upper()}', sub = True)
        sleep(1)

        funcion = getattr(__builtins__, funcion, None)
        print(f"\033[47m\033[30m{funcion.__doc__}\033[0m")

#ayuda()

help(str)