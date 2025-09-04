import requests
import json
import csv
from os import system

system('clear')

menu = '''
Datos disponibles:
     1. Género 
     2. Nombre (título, nombre, apellido)
     3. Ubicación (calle, ciudad, estado, país, código postal, zona horaria)
     4. Correo electrónico
     5. Inicio de sesión (nombre de usuario, contraseña)
     6. Registrado (fecha, edad)
     7. Fecha de nacimiento (fecha, edad)
     8. Teléfono 
     9. Celular
    10. Identificación (Tipo de documento, Número del documento)
    11. Foto
    12. Nacionalidad
'''

def leer_candidad(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print('Ingresa un numero que si no peto!')

def leer_datos(mensaje):
    while True:
        print(menu)
        datos = input(mensaje).split(',')
        datos = [i.strip() for i in datos]
        for i in datos:
            if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                print('\nIngrese opciones validas')
                break
        else:  
            return renombrar(list(dict.fromkeys(datos)))
        
def renombrar(datos):
    for indice, valor in enumerate(datos):
        if valor == '1':
            datos[indice] = 'gender'
        elif valor == '2':
            datos[indice] = 'name'
        elif valor == '3':
            datos[indice] = 'location'
        elif valor == '4':
            datos[indice] = 'email'
        elif valor == '5':
            datos[indice] = 'login'
        elif valor == '6':
            datos[indice] = 'registered'
        elif valor == '7':
            datos[indice] = 'dob'
        elif valor == '8':
            datos[indice] = 'phone'
        elif valor == '9':
            datos[indice] = 'cell'
        elif valor == '10':
            datos[indice] = 'id'
        elif valor == '11':
            datos[indice] = 'picture'
        elif valor == '12':
            datos[indice] = 'nat'

    return datos

def guardar_json(respuesta_json, nombre_archivo='datos_usuarios.json'):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(respuesta_json, archivo, indent=4, ensure_ascii=False)

def guardar_csv(respuesta_json, nombre_archivo='datos_usuarios.csv'):
    # Obtener los campos del primer usuario
    campos = list(respuesta_json['results'][0].keys())
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        # Escribir encabezados
        escritor.writerow(campos)
        # Escribir cada usuario
        for usuario in respuesta_json['results']:
            escritor.writerow(usuario.values())

def generar_ususario(cantidad, datos):
    url = f'https://randomuser.me/api/?results={cantidad}&inc={','.join(datos)}&noinfo'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        print(f'\nSe generaron {cantidad} usuarios')
        for usuario in respuesta_json['results']:
            if 'gender' in datos: print(f'Género: {usuario["gender"]}')
            if 'name' in datos: print(f'Nombre: {usuario["name"]["title"]} {usuario["name"]["first"]} {usuario["name"]["last"]}')
            if 'location' in datos: print(f'Ubicación: {usuario["location"]["street"]['name']}, {usuario["location"]["street"]['number']} - {usuario["location"]["city"]}, {usuario["location"]["state"]}')
            if 'email' in datos: print(f'correo electrónico: {usuario["email"]}')
            if 'login' in datos: print(f'Inicio de sesión: {usuario["login"]["username"]} - {usuario["login"]["password"]}')
            if 'dob' in datos: print(f'Fecha de nacimiento: {usuario["dob"]['date']} - {usuario['dob']["age"]} años')
            if 'registered' in datos: print(f'Registrado: {usuario["registered"]["date"]} - {usuario["registered"]["age"]} años')
            if 'phone' in datos: print(f'Teléfono: {usuario["phone"]}')
            if 'cell' in datos: print(f'Celular: {usuario["cell"]}')
            if 'id' in datos: print(f'Identificación: {usuario["id"]['name']} - {usuario["id"]['value']}')
            if 'picture' in datos: print(f'Foto: {usuario["picture"]["medium"]}')
            if 'nat' in datos: print(f'Nacionalidad: {usuario["nat"]}')
            print()
        return respuesta_json
    else:
        print('Error al obtener respuesta')



cantidad = leer_candidad('Cauntos usuarios deseas generar?: ')
datos = leer_datos('Que datos deben tener los usuarios? (1, 2,...): ')
respuesta_json = generar_ususario(cantidad, datos)
respuesta = input('Te gustaria guardar los datos en un archivo? (s/n): ')
if respuesta.lower() in ['si', 'yes', 's', 'y']:
   while True: 
    formato = input('En que formato te gustaria guardarlo? (json, csv): ')
    if formato.lower() in ['json', 'csv']:
        if formato.lower() == 'json':
            guardar_json(respuesta_json)
            print('Archivo guardado con éxito')
            break
        elif formato.lower() == 'csv':
            guardar_csv(respuesta_json)
            print('Archivo guardado con éxito')
            break
    else:
        print('Ingresa un formato valido')
else:
    print('Archivo no guardado')