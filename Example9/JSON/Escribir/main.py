import json

dicctionary = [
    {
        "table":12,
        "chair":14,
        "id":567,
    },{
        "table":44,
        "chair":10,
        "id":56,
    }
]

# pasamos el dicionario a un objeto tipo json
things = json.dumps(dicctionary, indent=4)

# usamos open para abrir el archivo o para generarlo si no existe y abrirlo
file = open("informacion.json","w")

# escribimos sobre todo el archivo (recomendedo)
file.write(things)

# cerramos el archivo
file.close()