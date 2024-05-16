from datetime import datetime
def registrarEntrada(datos):
    datos = list(datos)
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    vehiculo = input("ingresa el nombre del vehiculo ")
    placa = input("ingresa la placa del vehiculo ")
    for i in range(len(datos)):
        if placa == datos[i]["placa"]:
            if datos[i]["salio"] == False:
                print("ese vehiculo todavia no a salido ")
                return datos
    datos.append(
            {
            "vehiculo":vehiculo,
            "placa":placa,
            "fecha_entrada":str(fecha),
            "salio":False,
            "fecha_salida":"",
            "cobrado":0
        }
    )
    return datos

def registrarSalida(datos,tarifa_actual):
    datos = list(datos)
    fecha = datetime.now()
    fecha = fecha.replace(microsecond=0)
    placa = input("ingresa la placa del vehiculo ")
    for i in range(len(datos)):
        if placa == datos[i]["placa"]:
            datos[i]["fecha_salida"] = str(fecha)
            if datos[i]["salio"] == False:
                pago = input("si pago el dueño al salir? (si o no) ")
                pago = True if pago.lower() == "si" else False
                datos[i]["salio"] = True
                if pago:
                    try:
                        horas = int(input("cuantas horas estubo parqueado "))
                        if horas < 1:
                            print("ese valor no es valido")
                            return datos
                    except Exception:
                        print("ese valor no es valido")
                        return datos
                    datos[i]["cobrado"] = int(tarifa_actual[0])*horas
                    return datos
            else:
                print("ese vehiculo ya saio")
                return datos
    print("esa placa no se encontro ")
    return datos

def historialVehiculos(datos):
    datos = list(datos)
    for i in datos:
        print("")
        for j in i:
            print(j,":",i[j])

def totalRecaudado(datos):
    datos = list(datos)
    total = 0
    for i in datos:
        total += i["cobrado"]
    print("")
    print("el total recaudado ha sido de",total)

def vehiculosParqueados(datos):
    datos = list(datos)
    print("los vehiculos parqueados ahora son")
    for i in datos:
        if not(i["salio"]):
            print("")
            print(i["vehiculo"])
            print(i["placa"])