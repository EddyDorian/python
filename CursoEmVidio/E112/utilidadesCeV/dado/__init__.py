def leerDinero(mensaje):
    import re

    while True:
        numero = input(mensaje)

        if re.match(r'\d+([\,.]\d+)?', numero):
            numero = numero.replace(',', '.')
            return float(numero)
        
        print(f'\033[91mEl valor "{numero.upper()}" es invalido, ingrese un valor numerico!\033[0m')