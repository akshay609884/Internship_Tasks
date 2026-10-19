# 16 Caesar Cipher

# Hacker Rank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    result = []
    
    # Step 2: Loop through each character in the string
    for char in s:
        # Handle lowercase letters
        if 'a' <= char <= 'z':
            # Shift within the 0-25 range relative to 'a', then convert back to character
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            result.append(new_char)
        # Handle uppercase letters
        elif 'A' <= char <= 'Z':
            # Shift within the 0-25 range relative to 'A', then convert back to character
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
            result.append(new_char)
        # Non-alphabetical characters remain unchanged
        else:
            result.append(char)
            
    # Step 3: Join the list into a single string output
    return "".join(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
