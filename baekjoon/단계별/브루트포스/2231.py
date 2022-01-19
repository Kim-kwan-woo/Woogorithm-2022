import sys

def solution(N):
    for i in range(N):
        numList = list(str(i))
        totalSum = i + sum(list(map(int, numList)))

        if totalSum == N:
            return i

    return 0


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))