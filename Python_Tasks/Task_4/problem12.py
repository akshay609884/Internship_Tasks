# 12 Introduction to Sets
# Hacker Rank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    different_heights = set(array)
    return sum(different_heights)/len(different_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)