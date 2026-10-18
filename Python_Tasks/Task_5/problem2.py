# 2 String Split and Join
#  Hacker Rank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    words = line.split()
    new_words ="-".join(words)
    return new_words   

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)