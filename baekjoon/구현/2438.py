import sys

def solution(N):
    for i in range(1, N+1):
        print("*"*i)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    solution(N)
