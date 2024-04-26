num = int(input("ingresa un numero "))
primo = False
for i in range(2, num):
        if num%i != 0:
            primo = True
        else:
            primo = False
            break

if primo:
    print("es un numero primo")
else:
    print("no es un numero primo")