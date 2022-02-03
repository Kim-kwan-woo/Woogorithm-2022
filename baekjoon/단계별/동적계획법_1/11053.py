import sys

def solution():
    answer = [1] * N

    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                answer[i] = max(answer[i], answer[j]+1)

    return max(answer)

        


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().split()))
    print(solution())

