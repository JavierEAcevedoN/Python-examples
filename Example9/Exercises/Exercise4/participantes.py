def registrar_participante(datos):
    datos = dict(datos)
    nombre = input("ingresa el nombre del participante ")
    documento = input("ingresa el documento del participante ")
    cargo = input("ingresa el cargo del participante ")
    try:
        edad = int(input("ingresa la edad del participante "))
    except Exception:
        print("ese valor no es valido")
        return datos
    print("El participante ya pago? (si o no)")
    opc = ""
    opc = input("ingresa la edad del participante ")
    pago = True if opc.lower() == "si" else False
    datos["participantes"].append(
        {
            "nombre":nombre,
            "documento":documento,
            "edad":edad,
            "cargo":cargo,
            "pago":pago
        }
    )
    print("participante resgistrado")
    return datos

def eliminar_participante(datos):
    datos = dict(datos)
    doc = input("ingresa el documento del participante ")
    legth = len(datos["participantes"])
    for i in range(legth):
        if datos["participantes"][i]["documento"] == doc:
            if datos["participantes"][i]["pago"] == False:
                datos["participantes"].pop(i)
                print("participante eliminado")
                return datos
            else:
                print("ese participante ya pago")
                return datos
    print("no se encontro a ese participante")
    return datos

def pagar_participante(datos):
    datos = dict(datos)
    doc = input("ingresa el documento del participante ")
    legth = len(datos["participantes"])
    for i in range(legth):
        if datos["participantes"][i]["documento"] == doc:
            if datos["participantes"][i]["pago"] == False:
                datos["participantes"][i]["pago"] = True
                print("participante pagado")
                return datos
            else:
                print("ese participante ya pago")
                return datos
    print("no se encontro a ese participante")
    return datos

def cuales_participantes_nopago(datos):
    datos = dict(datos)
    for i in datos["participantes"]:
        if i["pago"] == False:
            print(i["nombre"])
    return datos

def cuantos_participantes_nopago(datos):
    datos = dict(datos)
    count = 0
    for i in datos["participantes"]:
        if i["pago"] == False:
            count += 1
    print(f"de {len(datos['participantes'])} participantes no han pagado {count}")
    return datos

def participantes_mes(datos):
    datos = dict(datos)
    for i in datos["participantes"]:
        print(i["nombre"])
    return datos