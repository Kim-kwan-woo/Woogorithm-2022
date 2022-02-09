import sys

def solution():
    multi = [1]*(N+1)

    for i in range(1, N+1):
        multi[i] = multi[i-1]*i

    return multi[N]//(multi[K]*multi[N-K])

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    
    print(solution())
    