import sys

def solution(n):

    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i-1] == True:
            for j in range(2*i, n-1, i):
                sieve[j-1] = False

    primeNumber1 = [i for i in range(2, n+1) if sieve[i-1] and i <= n//2]
    primeNumber2 = [i for i in range(2, n+1) if sieve[i-1] and i > n//2]
    
    if primeNumber1[-1] == n//2:
        return str(primeNumber1[-1]) + " " +  str(primeNumber1[-1])

    for i in range(len(primeNumber1)-1, -1, -1) :
        if (n - primeNumber1[i]) in primeNumber2:
            return str(primeNumber1[i]) + " " + str(n-primeNumber1[i])
    

    
if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        n = int(sys.stdin.readline().rstrip())
        answer.append(solution(n))

    for i in answer:
        print(i)
