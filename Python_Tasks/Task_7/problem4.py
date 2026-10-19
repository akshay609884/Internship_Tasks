# 4 Funny String
# Hacker Rank Link: https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    # Step 1: Create the reversed version of the string
    s_rev = s[::-1]
    
    # Step 2: Compare absolute ASCII differences between adjacent elements
    for i in range(1, len(s)):
        diff_original = abs(ord(s[i]) - ord(s[i - 1]))
        diff_reversed = abs(ord(s_rev[i]) - ord(s_rev[i - 1]))
        
        # If any difference doesn't match, it's not a funny string
        if diff_original != diff_reversed:
            return 'Not Funny'
            
    return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
