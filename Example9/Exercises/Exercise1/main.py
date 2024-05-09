""" Una empresa requiere un sistema para controlar el ingreso de los empleados diariamente a la empresa. Para esto se requiere un menú con las siguientes funcionalidades:

    Registrar empleado
    Listar todos los empleados
    Modificar empleados
    Despedir empleados (Esta función no elimina al empleados solo cambia su estado)
    Registrar entrada empleados
    Registrar salida de empleados

Para que el aplicativo funcione correctamente se debe tener en cuenta:

    Los empleados son registrados y manipulados en archivos de tipo json
    la entrada es a las 8:00 am y la salida a las 6:00 pm por lo tanto a los empleados se les marca advertencia cuando llegan después de la hora o salen antes de la hora. 
    Cada entrada y salida de empleados se debe registrar en un archivo txt o csv añadiendo línea a línea cada registro y no se debe modificar ni reescribir. Si el registro de entrada o salida aplica para alguna advertencia se debe marcar en el archivo también. """

import json
import csv
import datetime

file_json = open("empleados.json")
empleados = json.load(file_json)
file_csv = open("registroHora.csv")
registro = csv.DictReader(file_csv)

def registrarEmpleados(Empleado):
    Empleado = list(Empleado)

    nombre = input("ingresa el nombre del Empleado ")

    direccion = input("ingresa la dirección del Empleado ")

    telefono = input("ingresa el teléfono del Empleado ")

    correo = input("ingresa el correo del Empleado ")

    Despedido = False

    if nombre or direccion or telefono or correo == " ":
        return
    
    Empleado.append(
        {
            "Nombre":nombre,
            "Direccion":direccion,
            "Telefono":telefono,
            "Correo":correo,
            "Despedido":Despedido
        }
    )
    
    new_empleado = json.dumps(Empleado, indent=4)
    file_json = open("empleados.json","w")
    file_json.write(new_empleado)
    file_json.close()

def listartodosempleados(Empleado):
    Empleado = list(Empleado)
    count = 1
    for i in Empleado:
            print(count, i["Nombre"])
            count += 1

def modificarEmpleados(Empleado):
    Empleado = list(Empleado)
    num = int(input("ingresa el numero del Empleado para modificar "))-1
    for i,j in Empleado[num].items():
        print(i,j)

    direccion = input("ingresa la dirección del Empleado ")

    telefono = input("ingresa el teléfono del Empleado ")

    correo = input("ingresa el correo del Empleado ")

    Despedido = False

    Empleado[num].update(
        {
            "Direccion":direccion,
            "Telefono":telefono,
            "Correo":correo,
            "Despedido":Despedido
        }
    )

    mod_empleado = json.dumps(Empleado, indent=4)
    file_json = open("empleados.json","w")
    file_json.write(mod_empleado)
    file_json.close()

def despedirEmpleados(Empleado):
    Empleado = list(Empleado)
    num = int(input("ingresa el numero del Empleado para despedirlo "))-1
    for i,j in Empleado[num].items():
        print(i,j)
    choice = input("seguro de que quiere despedir a este empleado? (si o no) ")
    if choice.lower() == "no":
        return
    else:
        Empleado[num].update(
            {
                "Despedido":True
            }
        )
        des_empleado = json.dumps(Empleado, indent=4)
        file_json = open("empleados.json","w")
        file_json.write(des_empleado)
        file_json.close()

def HoraEmpleado(Empleado,Registro):
    nombre = input("ingresa tu nombre ")
    Empleado = list(Empleado)
    registro_empleados = list(Registro)
    esta = False
    hora = datetime.datetime.now()
    if hora.hour > 13:
        hora_am = f"{(hora.hour)-12}:{hora.minute} am"
        hora_pm = f"{(hora.hour)-14}:{hora.minute} pm"
    else:
        hora_am = f"{hora.hour}:{hora.minute} am"
        hora_pm = f"{(hora.hour)-2}:{hora.minute} pm"
    for i in Empleado:
        if i["Nombre"] == nombre:
            esta = True
    if esta:
        registro_empleados.append(
            {
            'Empleado': nombre, 'Hora_entrada': hora_am, 'Hora_Salida': hora_pm
            }
        )
        file_csv = open("registroHora.csv","w")
        columnas = ["Empleado","Hora_entrada","Hora_Salida"]
        escritor = csv.DictWriter(file_csv,fieldnames=columnas)
        escritor.writeheader()
        for r in registro_empleados:
            escritor.writerow(r)
        file_csv.close()
        print("hora registrada con exito")
        return registro_empleados
    else:
        print("ese empleado no se encuentra registrado")

while True:
    choice = -1
    choice = int(input("""
ingresa la opcion: 
(1) Registrar Empleados.
(2) Listar Empleados
(3) Modificar Empleados
(4) Despedir empleados
(5) Registrar hora empleados
(6) Terminar. """))
    if choice == 1:
        registrarEmpleados(empleados)
    elif choice == 2:
        listartodosempleados(empleados)
    elif choice == 3:
        modificarEmpleados(empleados)
    elif choice == 4:
        despedirEmpleados(empleados)
    elif choice == 5:
        registro = HoraEmpleado(empleados,registro)
    elif choice == 6:
        print("terminando proceso")
        break