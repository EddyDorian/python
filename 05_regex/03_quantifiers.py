###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

print("\n--------------")

##
print('\nEJERCICIO 1:\n')
##
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

### Completa aquí
texto = "El bambú es alto, El zambo es un animal, El sabio es inteligente"
patron = r'\b\w*a*b\w*\b'
resultado = re.finditer(patron, texto, flags = re.IGNORECASE)
contador = 0
print('Nro.', 'Palabra')
for indice, palabra in enumerate(resultado):
    print(f'{indice + 1:<4} {palabra.group()}')
    contador += 1
print('=' * 25)
print(f'Se encontraron {contador} palabras')

print("\n--------------\n")

# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

print("\n--------------")

##
print('\nEJERCICIO 2:\n')
##
# Haz opcional que aparezca un +34 en el siguiente texto
# phone = "+34 688999999"

### Completa aquí
phone = "+34 688999999"
patron = r'(\+34\s)?\d{9}'
respuesta = re.search(patron, phone)
print('El numero es correcto.') if respuesta else print('El numero no es correcto.')   

print("\n--------------\n")

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)