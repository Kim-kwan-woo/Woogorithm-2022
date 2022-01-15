import sys

def solution(M, N):

    sieve = [True] * N

    m = int(N ** 0.5)
    for i in range(2, m+1):
        if sieve[i-1] == True:
            for j in range(2*i, N+1, i):
                sieve[j-1] = False

    primeNumbers = [i for i in range(2, N+1) if (sieve[i-1] and (i >= M and i <=N))]

    if primeNumbers:
        print(sum(primeNumbers)) 
        print(primeNumbers[0])
    else:
        print('-1')
    

    
if __name__ == "__main__":
    M = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    solution(M, N)