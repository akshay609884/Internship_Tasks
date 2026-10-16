# 6 Find the Runner-Up Score!
# Hacker Rank Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
unique_score = sorted(set(arr))
print(unique_score[-2])   
