# 20 Super Reduced String

# Hacker Rank LinK: https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    stack = []
    
    # Process each character in the input string
    for char in s:
        # If the stack has items and the current character matches the last added item
        if stack and stack[-1] == char:
            stack.pop()  # Remove the matching adjacent pair
        else:
            stack.append(char)  # Push the character onto the stack
            
    # If the stack is empty after reductions, return the required fallback string
    if not stack:
        return "Empty String"
        
    return "".join(stack)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
