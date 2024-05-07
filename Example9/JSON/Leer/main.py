import json

file = open("informacion.json")
users = json.load(file)

for user in users:
    print(f"Nombre del usuario {user['name']} edad {user['age']} carro {user['car']}")
file.close()