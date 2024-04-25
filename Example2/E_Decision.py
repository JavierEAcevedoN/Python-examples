# son estructuras que hacen algo si la condicion es cierta o si no

# aqui se escribe verdadero ya que la condicion es verdadera
if True:
    print("verdadero")

# aqui se escribe falso ya que la condicion no se cumple
if False:
    print("verdadero")
else:
    print("Falso")

# aqui hay una estructura condicional multiple

edad = 40

if edad < 14:
    print("eres un niño")
elif 14 <= edad < 20:
    print("eres un adolecente adulto")
else:
    print("eres un adulto")

# tambien las condicionales se pueden usar para asignacion

mayorono = "si" if 30>10 else "no"
print(mayorono)