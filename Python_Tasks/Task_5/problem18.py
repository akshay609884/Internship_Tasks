
# 18 The Minion Game

# Hacker Rank LInk: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        # If the character is a vowel, Kevin gets the points
        if string[i] in vowels:
            kevin_score += length - i
        # Otherwise, Stuart gets the points
        else:
            stuart_score += length - i

    # Determine the winner
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
