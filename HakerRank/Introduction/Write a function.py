def is_leap(year):
    leap = False
    if year/4 == int(year/4):
        if year/100 != int(year/100):
            leap = True
    if year/400 == int(year/400):
        leap = True    
    return leap

year = int(input())
print(is_leap(year))