# 19 Weighted Uniform Strings

# Hacker Rank LinK:  https://www.hackerrank.com/challenges/weighted-uniform-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    possible_weights = set()
    
    current_weight = 0
    prev_char = ''
    
    # Step 1: Scan the string once to collect all valid weights
    for char in s:
        # Calculate the base weight of the character ('a' -> 1, 'b' -> 2, etc.)
        weight = ord(char) - ord('a') + 1
        
        # If the character matches the previous one, accumulate the weight
        if char == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = char
            
        # Add the weight to our set
        possible_weights.add(current_weight)
        
    # Step 2: Answer each query by performing a fast O(1) set lookup
    results = []
    for q in queries:
        if q in possible_weights:
            results.append("Yes")
        else:
            results.append("No")
            
    return results    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
