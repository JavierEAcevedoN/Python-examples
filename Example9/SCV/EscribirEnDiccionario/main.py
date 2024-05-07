from csv import DictWriter

personas = [
    {"nombre":"Juan","apellido":"Perez","edad":30},
    {"nombre":"Juan","apellido":"Perez","edad":30},
    {"nombre":"Juan","apellido":"Perez","edad":30}
]
nombres_columnas = ["nombre","apellido","edad"]

with open("personas.scv",mode="w", newline="") as archivo_csv:
    escritor = DictWriter(archivo_csv, fieldnames=nombres_columnas)
    escritor.writeheader()
    for persona in personas:
        escritor.writerow(persona)

archivo_csv.close()