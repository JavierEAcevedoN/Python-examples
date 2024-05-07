from csv import DictReader

with open("personas.scv","r") as file:
    lector = DictReader(file)
    for i in lector:
        print(i)