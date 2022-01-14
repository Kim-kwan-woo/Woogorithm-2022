import sys

def solution(X, numList):
    for i in numList:
        if i < X:
            print(i, end=" ")

if __name__ == "__main__":
    N, X = map(int, sys.stdin.readline().split())
    numList = list(map(int, sys.stdin.readline().split()))
    solution(X, numList)
