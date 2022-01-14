import sys

def solution(N, score):
    maxScore = max(score)
    newScore = [(i/maxScore)*100 for i in score ]

    return sum(newScore)/N


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    score = list(map(int, sys.stdin.readline().split()))

    print(solution(N, score))