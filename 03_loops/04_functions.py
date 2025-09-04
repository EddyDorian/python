###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# # Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_modo=True, gatos=40)

print('\nEjercicios')

print("\n--------------")

# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora

### Completa aquí
def leer_numero(mensaje):
    """
    Solicita al usuario que ingrese un número entero y continúa pidiendo hasta que se ingrese un valor válido.

    Returns:
        int: El número entero ingresado por el usuario.

    Ejemplos:
        >>> leer_numero()
        Ingresa un numero: abc
        Introduce un numero que si no PETO!
        Ingresa un numero: 123
        123
    """
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            print('Introduce un numero que si no PETO!')

def tabla_de_multiplicar_de(numero):
    """
    Genera e imprime la tabla de multiplicar del número especificado.

    Args:
        numero (int): El número para el cual se generará la tabla de multiplicar.

    Returns:
        None: La función solo imprime los resultados, no retorna ningún valor.

    Ejemplos:
        >>> tabla_de_multiplicar_de(5)
        5 x 1  = 5
        5 x 2  = 10
        5 x 3  = 15
        5 x 4  = 20
        5 x 5  = 25
        5 x 6  = 30
        5 x 7  = 35
        5 x 8  = 40
        5 x 9  = 45
        5 x 10 = 50
    """
    for multiplicando in range(1, 11):
        print(f'{numero} x {multiplicando:<2} = {numero * multiplicando}')

def buscar_el_mayor(*args):
    """
    Encuentra el número más grande entre los argumentos proporcionados.

    Args:
        *args: Variable número de argumentos numéricos

    Returns:
        El número más grande entre todos los argumentos proporcionados.

    Ejemplos:
        >>> buscar_el_mayor(5, 2, 9, 1)
        9
        >>> buscar_el_mayor(1)
        1
        >>> buscar_el_mayor(5, 5, 5)
        5
    """
    mayor = args[0]
    for numero in args:
        if numero > mayor:
            mayor = numero
    return mayor

def factorial_de(numero=0):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        numero (int, optional): El número para calcular su factorial. 
                              Por defecto es 0.

    Returns:
        int or None: El factorial del número si es no negativo, None si es negativo.

    Ejemplos:
        >>> factorial_de(5)
        120
        >>> factorial_de(0)
        1
        >>> factorial_de(-1)
        None
        >>> factorial_de()
        1
    """
    if numero < 0: return None
    if numero == 0: return 1
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

def numeros_primos_hasta(numero: int):
    """
    Genera una lista de todos los números primos desde 2 hasta el número especificado.

    Args:
        numero (int): El número límite hasta el cual se generan los primos.

    Returns:
        list: Lista de números primos encontrados, comenzando con 2.

    Ejemplos:
        >>> numeros_primos_hasta(10)
        [2, 3, 5, 7]
        >>> numeros_primos_hasta(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        >>> numeros_primos_hasta(2)
        [2]
    """
    primos = [2]
    posible_primo = 3
    while posible_primo <= numero:
        divisor = 3
        es_primo = True
        while divisor <= posible_primo ** 0.5:
            if posible_primo % divisor == 0:
                es_primo = False
            divisor += 2
        if es_primo: primos.append(posible_primo)
        posible_primo += 2
    return primos

def es_bisiesto(anhio: int):
    """
    Determina si un año es bisiesto según las reglas del calendario gregoriano.
    
    Un año es bisiesto si cumple alguna de estas condiciones:
    1. Es divisible por 4 Y no es divisible por 100
    2. Es divisible por 400
    
    Args:
        anhio (int): El año a verificar
        
    Returns:
        bool: True si el año es bisiesto, False si no lo es
        
    Examples:
        >>> es_bisiesto(2024)
        True
        >>> es_bisiesto(1900)
        False
        >>> es_bisiesto(2000)
        True
    """
    return (anhio % 4 == 0 and anhio % 100 != 0) or anhio % 400 == 0
    

numero = leer_numero('Ingresa un numero: ')
tabla_de_multiplicar_de(numero)
print()

mayor = buscar_el_mayor(15, 5, 25, 10, 20)
print(f'El mayor es: {mayor}')
print()

numero = leer_numero('Ingresa un numero: ')
factorial = factorial_de(numero)
if factorial:
  print(f'El factorial de {numero} es: {factorial}')
else:
   print('No existe el factorial de numeros negativos')
print()

numero = leer_numero('Ingresa un numero: ')
print(f'Los primos menores a {numero} son: {numeros_primos_hasta(numero)}')
print()

anhio = leer_numero('Ingrese un año: ')
if es_bisiesto(anhio):
   print(f'El {anhio} es bisiesto')
else:
   print(f'El {anhio} no es bisiesto')