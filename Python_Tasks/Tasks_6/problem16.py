# 16 Check Subset

# Hacker Rank LInk: https://www.hackerrank.com/challenges/py-check-subset/problem

# Read the number of test cases
for _ in range(int(input())):
    # Read set A
    num_a = int(input())
    set_a = set(map(int, input().split()))
    
    # Read set B
    num_b = int(input())
    set_b = set(map(int, input().split()))
    
    # Check if A is a subset of B and print the result
    print(set_a.issubset(set_b))
