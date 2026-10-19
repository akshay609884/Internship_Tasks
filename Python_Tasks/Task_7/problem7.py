# 7 Alphabet Rangoli

# Hacker Rank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase
    width = (size * 4) - 3
    
    # Range goes from (size-1) down to 0, and then back up to size
    # For size=3, row_indices will be: [2, 1, 0, 1, 2]
    row_indices = list(range(size - 1, 0, -1)) + list(range(size))
    
    for i in row_indices:
        # 1. Take letters from the outer edge down to current index 'i'
        left_letters = alphabet[i:size]
        
        # 2. Mirror them to get the right side
        full_letters = left_letters[::-1] + left_letters[1:]
        
        # 3. Join with hyphens and pad both sides to fill the width
        print("-".join(full_letters).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)