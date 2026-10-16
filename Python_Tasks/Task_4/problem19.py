# 19 Collections.Counter()
# Hacker Rank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    # Read the total number of shoes (not strictly needed for the logic, but consumed)
    num_shoes = int(input())
    
    # Read shoe sizes and count the inventory available for each size
    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)
    
    # Read the number of customers
    num_customers = int(input())
    
    total_earnings = 0
    
    # Process each customer transaction
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        # Check if the desired shoe size is still in stock
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1  # Reduce available inventory by 1
            
    print(total_earnings)
