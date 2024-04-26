# las funciones son un bloque de codigo que se puede ejecutar en cualquier parte del codigo

# estas son las partes de una funcion
def funcion(parametro):
    return  parametro

# las funciones se definen asi
def saludo(nombre):
    print("Bienvenido " + nombre)

saludo("javier")

# las funciones pueden tener parametros por defecto
def ejemplo1(nombre, lenguaje = "python"):
    print(nombre + " trabaja con " + lenguaje)

ejemplo1("javier")

ejemplo1("javier", "javascript")

# las funciones pueden tener un numero indeterminado de argumentos

def ejemplo2(*compras):
    print(compras)

ejemplo2("leche", "avena", "lentejas",)

# las funciones pueden tener un numero indeterminado de argumentos con sus nombres

def ejemplo3(**datos):
    print(datos)

ejemplo3(nombre = "Estavan", correo = "estevanelstudiante@gmail.com")

# las funciones pueden tener subfunciones

def ejemplo4(x):
    def int_funcion(y):
        return x+y
    return int_funcion

sum4 = ejemplo4(4)
total = sum4(4)
print(total)