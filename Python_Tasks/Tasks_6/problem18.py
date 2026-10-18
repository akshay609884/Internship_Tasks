# 18 Set Mutations

# Hacker Rank link: https://www.hackerrank.com/challenges/py-set-mutations/problem

# Read the number of elements in set A (not strictly needed)
_ = input()
# Read initial elements of set A
set_a = set(map(int, input().split()))

# Read the number of other sets
num_operations = int(input())

# Loop through each operation pair
for _ in range(num_operations):
    # Get the operation name (ignoring the length of the other set)
    operation_name = input().split()[0]
    # Read the elements of the other set
    other_set = set(map(int, input().split()))
    
    # Dynamically find the method on set_a and execute it with other_set
    getattr(set_a, operation_name)(other_set)

# Print the final sum of elements in set A
print(sum(set_a))
