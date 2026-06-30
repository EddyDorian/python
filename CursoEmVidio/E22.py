nombre = input('Ingrese su nombre: ')
print(nombre.upper())
print(nombre.lower())
c=0
for letra in nombre:
    if letra.isalpha():
        c += 1
print(c)
print(len(nombre.split()[0]))