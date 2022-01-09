import sys

def solution(N):
    totalSum = 0
    for i in range(1, N+1):
        totalSum += i
    return totalSum

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))

    