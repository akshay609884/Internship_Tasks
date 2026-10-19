# 10 CamelCase

# Hacker Rank LInk: https://www.hackerrank.com/challenges/camelcase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    if not  s:
        return 0
    word_count = 1
    for char in s:
        if char.isupper():
            word_count += 1
    return word_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

