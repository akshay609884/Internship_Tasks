# 15 Set .difference() Operation

# Hacker Rank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Read English newspaper details
n = int(input())
english_subs = set(map(int, input().split()))

# Read French newspaper details
m = int(input())
french_subs = set(map(int, input().split()))

# Find elements in English but NOT in French
only_english = english_subs.difference(french_subs)

# Print the total count of these unique students
print(len(only_english))
