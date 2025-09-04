import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

print("\n--------------")

##
print('\nEJERCICIO 1:\n')
##
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
# text = "omniman fanatico man bandana"

### Completa aquí
text = "omniman fanatico man bandana"
patron = r'\b[bfm]an\b'
resultado = re.finditer(patron, text, flags = re.IGNORECASE)
print('Nro.', 'Palabra')
for indice, palabra in enumerate(resultado):
  print(f'{indice + 1:<4} {palabra.group()}')

print("\n--------------\n")

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)

print("\n--------------")

##
print('\nEJERCICIO FINAL:\n')
##
# Con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png
# r'[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}'
## Buscar corner cases que no pasa y arreglarlo:
# "lo.que+sea@shopping.online"
# "michael@gov.co.uk"

### Completa aquí
correos = "lo.que+sea@shopping.online michael@gov.co.uk foxis65284@skate@ru.com 8rl6ub1ez0@wnbaldwy.com"
patron = r'\b[\w._%+-]+@(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*\b'


resultado = re.finditer(patron, correos, flags = re.IGNORECASE)
for indice, correo in enumerate(resultado):
  print(f'{indice + 1} {correo.group()}')
print("\n--------------\n")

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)