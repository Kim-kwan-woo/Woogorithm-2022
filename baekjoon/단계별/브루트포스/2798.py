import sys
from itertools import combinations

def solution(M, cards):
    cards = sorted([i[0]+i[1]+i[2] for i in list(combinations(cards, 3))], reverse=True)

    for i in cards:
        if i <= M:
            return i



if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    print(solution(M, cards))