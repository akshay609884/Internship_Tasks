# 17 Check Strict Superset

# Hacker Rank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Read the primary set A
set_a = set(map(int, input().split()))

# Read the number of other sets
num_other_sets = int(input())

is_strict_superset = True

# Check against each of the other sets
for _ in range(num_other_sets):
    other_set = set(map(int, input().split()))
    
    # The '>' operator checks for a strict superset condition
    if not (set_a > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)
