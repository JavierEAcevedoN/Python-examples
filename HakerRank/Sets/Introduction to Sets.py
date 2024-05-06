def average(array):
    array = set(array)
    suma = sum(array)
    div = len(array)
    return suma/div

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)