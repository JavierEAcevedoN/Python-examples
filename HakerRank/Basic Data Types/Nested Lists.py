estudiantes=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        estudiantes.append([name,score])
n = len(estudiantes)
for i in range(n):
    for j in range(i, n-1):
        if estudiantes[i][1] > estudiantes[j+1][1]:
            estudiantes[i], estudiantes[j+1] = estudiantes[j+1], estudiantes[i]
estudiantes_ordenados_puntuacion = []
for i in range(n):
    estudiantes_ordenados_puntuacion.append(estudiantes[i][1])
estudiantes_ordenados_puntuacion = set(estudiantes_ordenados_puntuacion)
estudiantes_ordenados_puntuacion = list(estudiantes_ordenados_puntuacion)
estudiantes_ordenados_puntuacion.sort()
estudiantes_ordenados = []
for i in range(n):
        if estudiantes[i][1] == estudiantes_ordenados_puntuacion[1]:
            estudiantes_ordenados.append(estudiantes[i][0])
estudiantes_ordenados.sort()
for i in estudiantes_ordenados:
    print(i)