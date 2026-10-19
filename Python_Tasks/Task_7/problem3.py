# 3 Mars Exploration
# Hacker Rank Link:  https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    altered_count = 0
    
    # Iterate through each character in the received string
    for i in range(len(s)):
        # Determine what character should be at this index
        if i % 3 == 0 or i % 3 == 2:
            expected = 'S'
        else:
            expected = 'O'
            
        # If the received character doesn't match the expected character, count it
        if s[i] != expected:
            altered_count += 1
            
    return altered_count
