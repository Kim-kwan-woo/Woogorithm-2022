import sys
from collections import deque

def solution():
    cards = deque([i for i in range(1, N+1)])

    while len(cards) != 1:
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    
    print(solution())

    
    