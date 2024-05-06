#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    list_of_words = s.split(" ")
    capital_words_list = [i.capitalize() if i.isalpha() else i for i in list_of_words ]
    return " ".join(capital_words_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()