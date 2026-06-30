from time import sleep

def factorial(numero, show = False):
    """
    -> Calcula el factorial de un numero dado.
    :param numero: Numero del que se calcula el factorial
    :param show: [Opcional] muestra el desarrollo del calculo
    :return: El resultado del calculo
    """
    producto = 1
    for i in range(numero, 0, -1):
        producto *= i
        if show:
            print(f'{i}', end='')
            if i != 1:
                print(f' * ', end='')
            else:
                print(f' = ', end='')
        
    return producto

#print(factorial(4))

print(factorial(5, True))

#help(factorial)