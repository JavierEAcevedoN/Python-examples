personas = [{"Nombre":"Pedro","Edad":54,"Hobbie":"Correr"}]

with open("personas.txt", "r") as file:
    resultado = file.readlines()
    for i in resultado:
        persona = i.split(",")
        persona[2] = persona[2][0:len(persona[2])-1]
        persona_dict={}
        persona_dict["Nombre"] = persona[0]
        persona_dict["Edad"] = int(persona[1])
        persona_dict["Hobbie"] = persona[2]
        personas.append(persona_dict)
for i in personas:
    print(i)

file.close()