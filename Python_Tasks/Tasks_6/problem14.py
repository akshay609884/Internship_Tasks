# 14 Set .intersection() Operation

# Hacker Rank LInK: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Read English newspaper details
n = int(input())
english_subs = set(map(int, input().split()))

# Read French newspaper details
m = int(input())
french_subs = set(map(int, input().split()))

# Find the intersection of both sets (students in both groups)
both_subs = english_subs.intersection(french_subs)

# Print the total count of these unique students
print(len(both_subs))
