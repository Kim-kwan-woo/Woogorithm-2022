import sys

def solution(A, B):
    return A + B

if __name__ == "__main__":
    sumList = []
    while True:
        try:
            A, B = map(int, sys.stdin.readline().split())
            sumList.append(solution(A, B))
        except:
            break

    for i in sumList:
        print(i)
