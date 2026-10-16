# 20 No Idea!
# Hacker Rank Link: https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
array = list(map(int, input().split()))
set_a = set(map(int,input().split()))
set_b = set(map(int,input().split()))
happiness = sum((i in set_a) - (i in set_b) for i in array)
print(happiness)