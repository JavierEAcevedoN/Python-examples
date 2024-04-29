"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abecedario_r3 = []

for i in range(0,len(abecedario)-1,3):
    abecedario_r3.append(abecedario[i])

for i in range(len(abecedario_r3)):
    abecedario.remove(abecedario_r3[i])

print(",".join(abecedario))