# 15 Lists
# Hacker Rank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Split the input into the command and its arguments
        command, *args = input().split()
        
        # Convert any arguments from strings to integers
        args = list(map(int, args))
        
        # Match the command and perform the corresponding action
        if command == "insert":
            my_list.insert(args[0], args[1])
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(args[0])
        elif command == "append":
            my_list.append(args[0])
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()
