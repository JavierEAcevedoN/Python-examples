def split_and_join(line):
    line = str(line)
    line_splited = line.split(" ")
    print("-".join(line_splited))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)