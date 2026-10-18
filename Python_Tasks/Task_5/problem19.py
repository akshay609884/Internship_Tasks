# 19 Merge the Tools!

# Hacker Rank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        
        # Remove duplicates while maintaining order
        # dict.fromkeys() creates a dictionary preserving the insertion order
        unique_chars = "".join(dict.fromkeys(chunk))
        
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
