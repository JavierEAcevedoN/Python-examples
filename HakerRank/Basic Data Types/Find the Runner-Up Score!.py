if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = set(arr)
arr = list(arr)

def ordenamiento(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i, n-1):
            if lista[i] > lista[j+1]:
                lista[i], lista[j+1] = lista[j+1], lista[i]
    print(lista[len(lista)-2])

ordenamiento(arr)