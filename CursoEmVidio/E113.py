def leerInt(txt):
    while True:
        try:     
            n = int(input(txt))  
        except ValueError:
            print('\033[91mERROR: Ingrese un numero ENTERO valido\033[0m')
            continue
        except KeyboardInterrupt:
            print('\n\033[91mEl usuario decicio terminar el programa\033[0m')
            return 0
        else:
            return n

def leerFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except ValueError:
            print('\033[91mERROR: Ingrese un numero REAL valido\033[0m')
        except KeyboardInterrupt:
            print('\n\033[91mEl usuario decicio terminar el programa\033[0m')
            return 0
        else:
            return n


ni = leerInt('Ingrese un numero Entero: ')
nf = leerFloat('Ingrese un numeor Float: ')
print(f"""
    El valor entero ingresado es: {ni}
    El valor real ingresado es: {nf}
""")
