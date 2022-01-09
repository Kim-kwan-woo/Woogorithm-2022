import sys

def solution(A, B):
    return A + B

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    sumList = []
    for i in range(N):
        A, B = map(int, sys.stdin.readline().split())
        sumList.append(solution(A, B))

    for i in range(N):
        print("Case #" + str(i+1) + ": " + str(sumList[i]))
