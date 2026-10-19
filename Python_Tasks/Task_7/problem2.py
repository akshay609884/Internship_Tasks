
# 2 The Captain's Room
# Hacker rank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    # Read group size K
    k = int(input())
    
    # Read the room numbers as a list of integers
    room_list = list(map(int, input().split()))
    
    # Create a set of unique room numbers
    room_set = set(room_list)
    
    # Mathematical Formula:
    # (Sum of unique rooms multiplied by K) minus (Actual sum of all rooms)
    # leaves you with the Captain's room multiplied by (K - 1)
    captains_room = (sum(room_set) * k - sum(room_list)) // (k - 1)
    
    print(captains_room)
