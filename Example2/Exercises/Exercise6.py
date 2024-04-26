edad = int(input("ingresa tu edad "))

if edad < 4:
    print("puedes entrar gratis")
elif 4 <= edad <= 18:
    print("tienes que pagar 5€")
else:
    print("tienes que pagar 10€")