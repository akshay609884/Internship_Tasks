# 8 Tuples

# Hacker Rank Link: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    raw_input = input()
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t  = tuple(integer_list)
    print(hash(t))