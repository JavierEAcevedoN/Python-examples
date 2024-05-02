# haciendo una loteria aleatoria
loteria = {"Carro","Avion","Casa","PS6","ZBOX720", "Helicoptero","TV","PC"}

for i  in range(len(loteria)):
    print(f"el {i+1}º jugador ha ganado el premio {loteria.pop()}")