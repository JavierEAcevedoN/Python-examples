""" Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.Preguntar por el NIF del cliente y mostrar sus datos.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.Terminar el programa. """

clientes = {}

def agregarcliente(cliente):
    cliente = dict(cliente)
    nif = input("ingresa el NIF del cliente ")

    nombre = input("ingresa el nombre del cliente ")

    dirección = input("ingresa la dirección del cliente ")

    teléfono = input("ingresa el teléfono del cliente ")

    correo = input("ingresa el correo del cliente ")

    preferente = input("el cliente es preferente? (si o no) ")
    preferente = True if preferente.lower() == "si" else False

    if nif == "":
        print("ingresa un NIF")
        return cliente
    else:
        cliente.update(
            {nif:{
                "Nombre":nombre,
                "Dirección":dirección,
                "Teléfono":teléfono,
                "Correo":correo,
                "Preferente":preferente
            }})
        return cliente

def eliminarcliente(cliente):
    cliente = dict(cliente)
    nif = input("ingresa el nif del cliente a eliminar ")
    cliente.pop(nif,None)
    return cliente

def mostrarcliente(cliente):
    cliente = dict(cliente)
    nif = input("ingresa el nif del cliente para ver la informacion ")
    print(f"NIF {nif}:")
    for i,j in cliente[nif].items():
        print(f"{i} = {j}")
    return cliente

def listartodosclientes(cliente):
    cliente = dict(cliente)
    for i in cliente:
            print(f"NIF: {i} Nombre: {cliente[i]["Nombre"]}")

def listarclientespreferentes(cliente):
    cliente = dict(cliente)
    for i in cliente:
        if cliente[i]["Preferente"] == True:
            print(f"NIF: {i} Nombre: {cliente[i]["Nombre"]}")
    return cliente

choice = 1

while True:
    choice = int(input("ingresa la opcion (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. "))
    if choice == 1:
        clientes = agregarcliente(clientes)
    elif choice == 2:
        clientes = eliminarcliente(clientes)
    elif choice == 3:
        mostrarcliente(clientes)
    elif choice == 4:
        listartodosclientes(clientes)
    elif choice == 5:
        listarclientespreferentes(clientes)
    elif choice == 6:
        print("terminando proceso")
        break