import sys

def solution(M, N):

    sieve = [True] * N

    m = int(N ** 0.5)
    for i in range(2, m+1):
        if sieve[i-1] == True:
            for j in range(2*i, N+1, i):
                sieve[j-1] = False

    return [i for i in range(M, N+1) if sieve[i-1] and i != 1]


    
if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    for i in solution(M, N):
        print(i)