from csv import writer

myData =[
    ["PrimerNombre","SegundoNombre","Grado"],
    ["Alex","Godoy","2"],
    ["Carlos","De la Torre","2"]
]

myFile = open("personas.csv","w",newline='')

with myFile:
    escritor = writer(myFile)
    escritor.writerows(myData)

myFile.close()