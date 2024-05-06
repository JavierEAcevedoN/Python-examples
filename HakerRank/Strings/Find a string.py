def count_substring(string, sub_string):
    string, sub_string = str(string), str(sub_string)
    if len(string) < len(sub_string):
        count = 0
    else:
        count = (1 if string.find(sub_string) == 0 else 0) + count_substring(string[1:], sub_string)
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)