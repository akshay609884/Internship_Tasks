# 20 Validating the Phone Number

# Hacker Rank Link:   https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

# Read the number of test cases
n = int(input())

# Loop through each phone number input
for _ in range(n):
    phone_number = input()
    
    # Check if the number matches the regex pattern
    # ^ ensures the match starts at the beginning
    # [789] matches either 7, 8, or 9 as the first digit
    # \d{9} matches exactly 9 remaining numerical digits
    # $ ensures no extra characters exist at the end
    if re.match(r'^[789]\d{9}$', phone_number):
        print("YES")
    else:
        print("NO")
