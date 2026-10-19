# 17 Separate the Numbers
# Hacker Rank LInk: https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    
    # A beautiful string must have at least 2 numbers, 
    # so the first number can at most be half the length of s.
    for i in range(1, (n // 2) + 1):
        # Extract the starting number substring
        first_num_str = s[:i]
        
        # Edge Case: Numbers cannot have leading zeros (unless the number itself is 0)
        if first_num_str[0] == '0' and len(first_num_str) > 1:
            continue
            
        first_num = int(first_num_str)
        
        # Build the sequence string dynamically starting from our first number
        temp_str = first_num_str
        next_num = first_num + 1
        
        while len(temp_str) < n:
            temp_str += str(next_num)
            next_num += 1
            
        # If the generated sequence matches the target string, we found our valid sequence
        if temp_str == s:
            print(f"YES {first_num}")
            return
            
    # If no starting number yields a valid consecutive sequence, it's not beautiful
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
