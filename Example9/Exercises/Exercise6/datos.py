import json
import csv

def cargar_json(ruta):
    datos = {}
    file = open(ruta,"r")
    datos = json.load(file)
    return datos

def guardar_json(datos, ruta):
    datos = dict(datos)
    diccionario = json.dumps(datos, indent=4)
    file = open(ruta,"w")
    file.write(diccionario)
    file.close()

def cargar_csv(ruta):
    file = open(ruta,"r")
    datos = csv.DictReader(file, delimiter=";")
    return datos

def guardar_csv(datos, ruta):
    datos = list(datos)
    file = open(ruta,"a")
    escritor = csv.writer(file)
    escritor.writerows(datos)
    file.close()