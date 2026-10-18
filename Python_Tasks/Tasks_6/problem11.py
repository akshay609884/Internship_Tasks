# 11 String Formatting

# Hacker Rank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Convert the number into decimal, octal, hex, and binary formats
        dec_val = str(i)
        oct_val = oct(i)[2:]
        hex_val = hex(i)[2:].upper()  # Hex letters must be capitalized
        bin_val = bin(i)[2:]
        
        # Print each value right-aligned to the maximum width using rjust()
        print(f"{dec_val.rjust(width)} {oct_val.rjust(width)} {hex_val.rjust(width)} {bin_val.rjust(width)}")



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)