import sys

def solution(n):

    sieve = [True] * 2*n

    m = int(2*n ** 0.5)
    for i in range(2, m+1):
        if sieve[i-1] == True:
            for j in range(2*i, 2*n+1, i):
                sieve[j-1] = False

    return len([i for i in range(n+1, 2*n+1) if sieve[i-1] and i != 1])


    
if __name__ == "__main__":
    answer = []
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            break

        answer.append(solution(n))


    for i in answer:
        print(i)
