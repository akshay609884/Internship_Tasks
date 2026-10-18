# 19 Company Logo
# Hacker Rank LInK: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
from collections import Counter

    
    # Count the frequencies of each character
counts = Counter(s)
    
    # Sort by frequency (negative value for descending) and then by character alphabetically
    # counts.items() returns pairs like ('b', 3)
sorted_chars = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    # Print the top 3 items
for char, count in sorted_chars[:3]:
    print(f"{char} {count}")
