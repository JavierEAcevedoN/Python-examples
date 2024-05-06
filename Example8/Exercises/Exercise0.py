Empresas = {

"Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

"Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

"Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

"Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

"Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

}

def mostarempresas(Empresas):
    for i in Empresas:
        for j in Empresas[i]:
            if j["departamento"] == "Recursos Humanos":
                if j["empleados"] > 10:
                    print(i)

def promedioempleados(Empresas):
    for i in Empresas:
        total = 0
        div = len(Empresas[i])
        for j in Empresas[i]:
            total += j["empleados"]
        print(total/div)

def doblerespectoventas(Empresas):
    for i in Empresas:
        val1 = 0
        val2 = 0
        for j in Empresas[i]:
            if j["departamento"] == "Ventas":
                val1 = j["empleados"]
            if j["departamento"] == "Operaciones":
                val2 = j["empleados"]
        if val2 > 2*val1:
            print(i)


def reorganizar(Empresas):
    reorganizado = {}
    for i in Empresas:
        print(Empresas[i])
    print(reorganizado)

# terminar
""" reorganizado.update(
    {
        "Departamentos": {
            "Recursos Humanos": [{"empresas":"Empresa 1", "empleados":"5"},{"empresas":"Empresa 2", "empleados":"10"},...]
        }
    }
) """

while True:
    choice = int(input("""
ingresa la opcion.
(1) Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos. 
(2) Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo). 
(3) Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas. 
(4) Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas sino por departamento.. 
(5) Salir. """))

    if choice == 1:
        clientes = mostarempresas(Empresas)
    elif choice == 2:
        clientes = promedioempleados(Empresas)
    elif choice == 3:
        doblerespectoventas(Empresas)
    elif choice == 4:
        reorganizar(Empresas)
    elif choice == 5:
        print("terminando proceso")
        break
    else:
        print("ingrese una opcion valida")