#  15 Word Order
# Hacker Rank Link : https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input())


dic = {}
for i in range(n):
    word = input()
    
    if word in dic:
        dic[word]+= 1
    else:
        dic[word] = 1
print(len(dic))
for i in dic.values():
    print(i, end = ' ') 


