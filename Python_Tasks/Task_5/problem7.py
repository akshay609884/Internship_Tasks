# 7 Symmetric Difference 
# Hacker Rank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
m_size = int(input())
m_set  = set(map(int, input().split()))

n_size = int(input())
n_set = set(map(int, input().split()))

sym_dif = sorted(m_set.symmetric_difference(n_set))

for i in sym_dif:
    print(i)
