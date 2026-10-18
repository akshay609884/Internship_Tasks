# 10 Designer Door Mat

# Hacker Rank link: https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    # Read the dimensions N (height) and M (width)
    N, M = map(int, input().split())
    
    # 1. Top half of the mat
    for i in range(1, N, 2):
        pattern = ".|." * i
        print(pattern.center(M, '-'))
        
    # 2. Middle WELCOME line
    print("WELCOME".center(M, '-'))
    
    # 3. Bottom half of the mat (reverse of the top)
    for i in range(N - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(M, '-'))
