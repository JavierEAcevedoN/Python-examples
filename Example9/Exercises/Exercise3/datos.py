import json

def leerJson(ruta):
    file = open(ruta,"r")
    dato = json.load(file)
    return dato

def guardarJson(list,ruta):
    file = open(ruta,"w")
    escribir = json.dumps(list, indent=4)
    file.write(escribir)