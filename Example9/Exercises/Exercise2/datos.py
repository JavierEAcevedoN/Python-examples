import json
import csv

def leerJson(ruta):
    file = open(ruta,"r")
    dato = json.load(file)
    return dato

def guardarJson(list,ruta):
    file = open(ruta,"w")
    escribir = json.dumps(list, indent=4)
    file.write(escribir)

def leerCSV(ruta):
    file = open(ruta,"r")
    lector = csv.reader(file)
    return lector

def guardarCSV(txt,ruta):
    file = open(ruta,"r")
    escribir = csv.writer(file)
    escribir.writerows(txt)