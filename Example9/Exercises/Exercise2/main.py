from datos import *
from registro import *
tarifa = leerCSV("tarifa.csv")
tarifa_actual = []
for i in tarifa:
    tarifa_actual = i
registro = leerJson("registro.json")

while True:
    choice = -1
    try:
        choice = int(input("""
ingresa la opcion: 
(1) Registrar entrada de vehiculo.
(2) Registar salida vehiculo.
(3) Mostrar historial de carros.
(4) Mostrar la cantidad de dinero recaudado.
(5) Mostrar los vehiculos parqueados en el momento.
(0) Terminar. """))
    except Exception:
        print("ese valor no es valido")

    if choice == 1:
        registro = registrarEntrada(registro)
    elif choice == 2:
        registro = registrarSalida(registro,tarifa_actual)
    elif choice == 3:
        historialVehiculos(registro)
    elif choice == 4:
        totalRecaudado(registro)
    elif choice == 5:
        vehiculosParqueados(registro)
    elif choice == 0:
        print("terminando proceso")
        break
    guardarJson(registro,"registro.json")