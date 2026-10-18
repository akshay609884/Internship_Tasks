# 12 Set .discard(), .remove() & .pop()
# Hacker Rank Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())

for _ in range(num_commands):
    # Split the input into the command name and optional arguments
    command, *args = input().split()
    
    # Convert args to integers if any exist (like the number to remove/discard)
    args = list(map(int, args))
    
    # Dynamically find the method on set 's' matching the command name and call it
    getattr(s, command)(*args)

# Print the sum of the remaining elements in the set
print(sum(s))
