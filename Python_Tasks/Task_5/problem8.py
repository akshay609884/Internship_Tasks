# 8 Set .add()

# Hacker Rank Link : https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
country_num = int(input())
country_name  = set()
for _ in range(country_num):
    country_name.add(input().strip())
print(len(country_name))
