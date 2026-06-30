from statistics import mean

def notas(*notas, sit=False):
    """
    Devuelve un diccionario con las notas analizadas
    :param notas: una o mas notas de los alumnos de un curso
    :param sit: [Opcional] permite mostrar la situacion del curso
    :retur: retorna un diccionario con:
            la Cantidad de notas analizadas,
            la nota mayor ingresada
            la nota menor ingresada
            el promedio de las notas analizadas
            [opcional] la situacion actual del curso
    """
    dic = {}
    dic['cantidad'] = len(notas)
    dic['mayor'] = max(notas)
    dic['menor'] = min(notas)
    dic['media'] = mean(notas)
    if sit:
        if dic['media'] < 5:
            dic['situacion'] = 'Mala'
        elif 5 <= dic['media'] < 7:
            dic['situacion'] = 'Razonable'
        elif dic['media'] >= 7:
            dic['situacion'] = 'Buena'
    
    return dic
    
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True) 
print(resp)

#help(notas)