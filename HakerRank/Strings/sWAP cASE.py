def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        s[i] = s[i].upper() if s[i].islower() else s[i].lower()
    return("".join(s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)