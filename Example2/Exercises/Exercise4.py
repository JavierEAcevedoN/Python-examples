edad = int(input("ingresa tu edad "))
ingresos = 0

if edad > 16:
    ingresos = int(input("ingresa tus ingresos "))
if ingresos >= 1000:
    print("si puedes tributar")
else:
    print("no puedes tributar")