def print_formatted(number):
    for i in range(1, number+1):
        padding = len(str(bin(number)[2:]))
        print(f'{i:>{padding}} {oct(i)[2:]:>{padding}} {hex(i)[2:].upper():>{padding}} {bin(i)[2:]:>{padding}}')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)