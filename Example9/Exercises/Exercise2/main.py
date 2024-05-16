""" Se necesita un aplicativo para controlar y cobrar la tarifa de un parqueadero. Para esto se requiere un menú con las siguientes funcionalidades:

    Registrar entrada con placa (Valor único e identificador)
    Marcar salida para cobrar
    consultar histórico de carros parqueados con hora salida y hora entrada de cada una de las visitas de cada carro y los valores cobrados.
    Consultar cantidades de dinero recaudado.
    saber cuales carros se encuentran parqueados en el momento.

Para que el aplicativo funcione correctamente se debe tener en cuenta:

    El valor de la tarifa por hora o fracción se debe registrar y leer desde un archivo txt o csv.
    El registro de carros, visitas se debe realizar en un archivo tipo json. Para cada carro se deben almacenar todas las visitas que haya hecho con entrada, salida y valor pagado. Además, se debe tener un atributo dedicado a saber si el valor fue pagado o no. """

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
(3) Mostrar historial de vehiculos.
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