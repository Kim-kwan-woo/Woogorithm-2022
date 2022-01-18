import sys

def solution(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * solution(N-1)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    print(solution(N))