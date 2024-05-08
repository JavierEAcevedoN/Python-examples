import json

def cargar_datos(ruta):
    datos = {}
    file = open(ruta,"r")
    datos = json.load(file)
    return datos

def guardar_datos(datos, ruta):
    datos = dict(datos)
    diccionario = json.dumps(datos, indent=4)
    file = open(ruta,"w")
    file.write(diccionario)
    file.close()