# 14 Anagram

# Hacker Rank LInK: https://www.hackerrank.com/challenges/anagram/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    n = len(s)
    
    # Step 1: If the string length is odd, it cannot be divided into two equal halves
    if n % 2 != 0:
        return -1
        
    # Step 2: Split the string into two equal halves
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Step 3: Count character frequencies in both halves
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Step 4: Calculate characters in s1 that are missing or deficient in s2
    # Python's Counter subtraction (count1 - count2) leaves only elements with positive counts
    diff = count1 - count2
    
    # The sum of these remaining frequencies is the minimum changes needed
    return sum(diff.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
