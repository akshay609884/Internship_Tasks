# 13 Sherlock and the Valid String

# Hacker Rank Link:  https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    # Step 1: Count occurrences of each character
    char_counts = Counter(s)
    
    # Step 2: Count the frequencies of those occurrences
    freq_counts = Counter(char_counts.values())
    
    # If all characters appear the same number of times, it's valid
    if len(freq_counts) == 1:
        return "YES"
        
    # If there are more than two distinct frequencies, it's impossible to fix with 1 delete
    if len(freq_counts) > 2:
        return "NO"
        
    # Extract the two frequencies and how many characters have them
    # Example format: keys = [freq1, freq2], values = [count1, count2]
    freqs = list(freq_counts.keys())
    
    f1, f2 = freqs[0], freqs[1]
    c1, c2 = freq_counts[f1], freq_counts[f2]
    
    # Case 1: The first frequency belongs to only one character, and reducing its count to 0 leaves it valid
    # Example: "aabbccdddd" (if we swap view) or "aabbccd" -> where one character appears exactly once
    if (c1 == 1 and f1 == 1) or (c2 == 1 and f2 == 1):
        return "YES"
        
    # Case 2: One frequency belongs to only one character, and removing 1 instance matches the other frequency
    # Example: "aabbccc" -> frequencies are 2 (appears 2 times) and 3 (appears 1 time). 3 - 1 == 2.
    if (c1 == 1 and f1 - 1 == f2) or (c2 == 1 and f2 - 1 == f1):
        return "YES"
        
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
