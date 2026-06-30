def aumentar(numero, porcentaje, formato = False):
    if formato:
        return moneda(numero + numero * (porcentaje / 100))
    return numero + numero * (porcentaje / 100)

def disminuir(numero, porcentaje, formato = False):
    if formato:
        return moneda(numero - numero * (porcentaje / 100))    
    return numero - numero * (porcentaje / 100)

def doble(numero, formato = False):
    if formato:
        return moneda(2 * numero)    
    return 2 * numero

def mitad(numero, formato = False):
    if formato:
        return moneda(numero / 2)
    return numero / 2

def moneda(numero):
    return f'Bs. {numero}'