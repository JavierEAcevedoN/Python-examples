from csv import DictReader

with open("personas.csv","r") as file:
    lector = DictReader(file)
    for i in lector:
        print(i)