def registrar_participante(datos):
    datos = dict(datos)
    nombre = input("ingresa el nombre del participante ")
    departamento = input("ingresa tu departamento ").lower()
    if departamento != "santander":
        print("solo se puede registrar si eres del departamento de santander")
    try:
        documento = int(input("ingresa el documento del participante "))
        edad = int(input("ingresa la edad del participante "))
        if edad < 18:
            print("los menores de edad no se pueden registrar")
            return datos
    except Exception:
        print("ese valor no es valido")
        return datos
    opc = -1
    try:
        opc = int(input("ingresa 1 para Atletismo, 2 para Ciclismo, 3 para Patinaje "))
    except Exception:
        print("ese valor no es valido")
        return datos
    if opc == 1:
        opc = "Atletismo"
    elif opc == 2:
        opc = "Ciclismo"
    elif opc == 3:
        opc = "Patinaje"
    for i in datos[opc]:
        if documento == i["documento"]:
            print("ese participante ya esta registrado en ese evento")
            return datos
    datos[opc].append(
        {
            "nombre":nombre.capitalize(),
            "documento":documento,
            "edad":edad,
        }
    )
    print("participante resgistrado")
    return datos

def listar_participantes(datos):
    datos = dict(datos)
    for i in datos:
        print("")
        print(i)
        for j in datos[i]:
            for k in j:
                print(k,":",j[k])
            print("")
    return datos

def mostrar_ranking(datos):
    datos = dict(datos)
    for i in datos:
        print("")
        print(i,":")
        for j in range(len(datos[i])):
            print("")
            for k in datos[i][j]:
                print(f"\t{k} : {datos[i][j][k]}")
            print(f"\tranking {j+1}º")
    return datos