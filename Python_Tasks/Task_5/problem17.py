# 17 No Idea!

# Hacker Rank LInk: https://www.hackerrank.com/challenges/no-idea/problem



# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# Read number of shoes (not strictly needed for calculation, but part of input)
num_shoes = int(input())

# Create a inventory counter of available shoe sizes
shoe_sizes = Counter(map(int, input().split()))

# Read number of customers
num_customers = int(input())

total_revenue = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    
    # If the size is in stock, make the sale
    if shoe_sizes[size] > 0:
        total_revenue += price
        shoe_sizes[size] -= 1  # Reduce stock by 1

print(total_revenue)

