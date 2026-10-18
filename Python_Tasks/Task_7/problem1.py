# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read English newspaper details
n = int(input())
english_subs = set(map(int, input().split()))

# Read French newspaper details
m = int(input())
french_subs = set(map(int, input().split()))

# Find elements in either set, but not in both
either_but_not_both = english_subs.symmetric_difference(french_subs)

# Print the total count of these unique students
print(len(either_but_not_both))

