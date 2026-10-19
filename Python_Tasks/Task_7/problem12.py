# 12 Making Anagrams

# Hacker Rank LInk: https://www.hackerrank.com/challenges/making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2


def makingAnagrams(s1, s2):
    # Write your code here
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Step 2: Combine all unique characters from both strings
    all_chars = set(count1.keys()).union(set(count2.keys()))
    
    # Step 3: Sum the absolute differences in frequencies
    deletions = 0
    for char in all_chars:
        deletions += abs(count1[char] - count2[char])
        
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
