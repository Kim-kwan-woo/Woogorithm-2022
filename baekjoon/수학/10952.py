import sys

def solution(A, B):
    return A + B

if __name__ == "__main__":
    sumList = []
    while True:
        A, B = map(int, sys.stdin.readline().split())

        if A == 0 and B == 0:
            break

        sumList.append(solution(A, B))

    for i in sumList:
        print(i)
