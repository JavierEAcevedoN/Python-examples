if __name__ == '__main__':
    s = input()
    alfanum = False
    alphabetic = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if(not alfanum):
            alfanum = i.isalnum()
        if(not alphabetic):
            alphabetic = i.isalpha()
        if(not digit):
            digit = i.isdigit()
        if(not lower):
            lower = i.islower()
        if(not upper):
            upper = i.isupper()
    print(alfanum)
    print(alphabetic)
    print(digit)
    print(lower)
    print(upper)