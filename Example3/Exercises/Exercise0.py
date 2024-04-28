def primos(num):
    for i in range(2, num):
        if num%i == 0:
            print("no es un numero primo")
            break
        else:
            print("es un numero primo")
            break

num = int(input("ingresa un numero "))
primos(num)