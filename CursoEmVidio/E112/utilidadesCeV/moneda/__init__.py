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
    return f'Bs. {numero:.2f}'

def resumen(precio, aumento, descuento):
    respuesta = f"""
    {'~' * 32}
    {f'RESUMEN':^32}
    {'~' * 32}
    {'Precio analizado:':<20} {moneda(precio):<15}
    {'Doble del Precio:':<20} {doble(precio, True):<15}
    {'Mitad del precio:':<20} {mitad(precio, True):<15}
    {f'{aumento}% de aumento:':<20} {aumentar(precio, aumento, True):<15}
    {f'{descuento}% de descuento:':<20} {disminuir(precio, descuento, True):<15}
    {'~' * 32}
    """
    return respuesta
