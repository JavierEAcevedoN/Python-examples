password = "campus2023"
while True:
    input_password = input("ingresa la contraseña ").lower()
    if input_password == password:
        print("contraseña correcta")
        break
    else:
        print("contraseña incorrecta")
