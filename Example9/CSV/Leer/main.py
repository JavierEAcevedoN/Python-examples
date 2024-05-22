from csv import reader

with open("personas.csv", "r") as file:
    resultado = reader(file)
    for i in resultado:
        print(i)

file.close()