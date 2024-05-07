personas = [{"Nombre":"Pedro","Edad":54,"Hobbie":"Correr"},
            {"Nombre":"Juan","Edad":23,"Hobbie":"Leer"},
            {"Nombre":"Nicolas","Edad":30,"Hobbie":"Nadar"},
            {"Nombre":"Maria","Edad":25,"Hobbie":"Patinar"},
            ]

with open("personas.txt", "w") as file:
    for i in personas:
        file.write(f'{i["Nombre"]},{i["Edad"]},{i["Hobbie"]}\n')

file.close()