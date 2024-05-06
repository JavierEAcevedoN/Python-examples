def print_rangoli(size):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    in_use = alph[:size][::-1]
    max_width = len('-'.join(list(in_use+in_use[::-1][1:])))
    for i in range(1,size+1):
        rangoli = in_use[:i]+in_use[:i][::-1][1:]
        if i!=1:
            rangoli = '-'.join(list(rangoli))
        print(rangoli.center(max_width,  '-'))
    for i in list(reversed(range(1,size))):
        rangoli = in_use[:i]+in_use[:i][::-1][1:]
        if i!=1:
            rangoli = '-'.join(list(rangoli))
        print(rangoli.center(max_width,  '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)