from csv import reader

with open("personas.scv", "r") as file:
    resultado = reader(file)
    for i in resultado:
        print(i)

file.close()