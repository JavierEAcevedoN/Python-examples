def registrar_evento(datos):
    datos = dict(datos)
    nombre = input("ingresa el nombre del evento ")
    locacion = input("ingresa el locacion del evento ")
    try:
        dia = int(input("ingresa la dia del evento "))
        if dia <= 0 or 31 <= dia:
            print("ese dia no es valido")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    datos["eventos"].append(
        {
            "nombre":nombre,
            "locacion":locacion,
            "dia":dia,
            "realizado":False
        }
    )
    print("evento resgistrado")
    return datos

def modificar_evento(datos):
    datos = dict(datos)
    try:
        dia = int(input("ingresa el dia del evento "))
        if dia <= 0 or 31 <= dia:
            print("ese dia no es valido")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    legth = len(datos["eventos"])
    for i in range(legth):
        if datos["eventos"][i]["dia"] == dia:
            nombre = input("ingresa el nombre del evento ")
            locacion = input("ingresa el locacion del evento ")
            datos["eventos"][i]["nombre"] = nombre
            datos["eventos"][i]["locacion"] = locacion
            return datos
    print("no se encontro ese evento")
    return datos

def finalizar_evento(datos):
    datos = dict(datos)
    try:
        dia = int(input("ingresa el dia del evento "))
        if dia <= 0 or 31 <= dia:
            print("ese dia no es valido")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    legth = len(datos["eventos"])
    for i in range(legth):
        if datos["eventos"][i]["dia"] == dia:
            if datos["eventos"][i]["realizado"] == False:
                datos["eventos"][i]["realizado"] = True
                print("evento terminado")
                return datos
            else:
                print("ese evento ya termino")
                return datos
    print("no se encontro ese evento")
    return datos

def eventos_mes(datos):
    datos = dict(datos)
    for i in datos["eventos"]:
        print(i["nombre"])
    return datos