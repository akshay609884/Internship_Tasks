# 15 Game of Thrones - I

# Hacker Rank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    char_counts = Counter(s)
    
    # Step 2: Count how many characters have an odd frequency
    odd_counts = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_counts += 1
            
    # Step 3: A palindrome anagram can have at most one character with an odd count
    if odd_counts <= 1:
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()


