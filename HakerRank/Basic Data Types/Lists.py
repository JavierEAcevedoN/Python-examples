if __name__ == '__main__':
    N = int(input())
    lista = []
for i in range(N):
    n = input("").split()
    if n[0] == "insert":
        lista.insert(int(n[1]),int(n[2]))
    if n[0] == "print":
        print(lista)
    if n[0] == "remove":
        lista.remove(int(n[1]))
    if n[0] == "append":
        lista.append(int(n[1]))
    if n[0] == "sort":
        lista.sort()
    if n[0] == "pop":
        lista.pop()
    if n[0] == "reverse":
        lista.reverse()