def minion_game(string):
    vowels = ["a","e","i","o","u"]
    kevin = 0
    stuart = 0
    n = len(string)
    for i,char in enumerate(string) :
        if char.lower() in vowels :
            kevin += n - i
        else :
            stuart += n - i
    if kevin > stuart :
        print("Kevin " + str(kevin) )
    elif stuart > kevin :
        print("Stuart " + str(stuart))
    else :
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)