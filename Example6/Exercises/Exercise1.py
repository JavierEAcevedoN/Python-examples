def primo():
    num = int(input("ingresa un numero "))
    primo = False
    for i in range(2,num):
        if num%i == 0:
            primo = True
            break
        else:
            primo = False
    if primo:
        print(f"el numero {num} no es primo")
    else:
        print(f"el numero {num} es primo")

def paroimpar():
    num = int(input("ingresa un numero "))
    if num%2==0:
        print(f"El numero {num} es par")
    else:
        print(f"El numero {num} es impar")


def lista():
    legth = int(input("ingresa el largo de la lista "))
    lista = []
    for i in range(legth):
        lista.append(int(input(f"ingresa el {i+1}º numero ")))
    return lista

def media(lista):
    div = 0
    for i in lista:
        div += i
    div /= len(lista)
    print(f"el promedio de la lista es de {div}")

def letra():
    letra = ("x","z")
    palabra = input("ingresa una palabra ")
    for i in letra:
        for j in palabra:
            if j == i:
                print(f"la palabra ingresada tiene la letra {i}")
                break

while True:
    choice = int(input("0 para salir, 1 para numeros primos, 2 para par o impar, 3 promedio de lista, 4 para buscar x y/o z en una palabra "))
    if choice == 0:
        break
    elif choice == 1:
        primo()
    elif choice == 2:
        paroimpar()
    elif choice == 3:
        media(lista())
    elif choice == 4:
        letra()