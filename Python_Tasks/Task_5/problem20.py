# 20 Piling Up 
# Hacker Rank link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

# Read number of test cases
for _ in range(int(input())):
    n = int(input())
    # Load cubes into a double-ended queue (deque)
    cubes = deque(map(int, input().split()))
    
    # Initialize the base with an infinitely large block
    last_picked = float('inf')
    possible = True
    
    # Process all cubes
    while cubes:
        # Compare left and right ends, pick the larger one
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.popright() if hasattr(cubes, 'popright') else cubes.pop()
            
        # If the picked cube is larger than the previous one, stacking fails
        if current > last_picked:
            possible = False
            break
            
        last_picked = current
        
    print("Yes" if possible else "No")
