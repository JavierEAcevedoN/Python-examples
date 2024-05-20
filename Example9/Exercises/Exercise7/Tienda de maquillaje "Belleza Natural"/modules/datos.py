import json
import csv

def leer_json(ruta):
    file = open(ruta,"r")
    leer = json.load(file)
    return leer

def guardar_json(ruta,archivo):
    escribir = json.dumps(archivo,indent=4)
    file = open(ruta,"w")
    file.write(escribir)

def leer_csv(ruta):
    file = open(ruta,"r")
    leer = csv.DictReader(file)
    leer = list(leer)
    return leer

def guardar_csv(ruta,archivo):
    file = open(ruta,"a")
    escribir = csv.writer(file)
    escribir.writerows(archivo)