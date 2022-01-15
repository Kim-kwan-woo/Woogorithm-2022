import sys

def solution(N):

    sieve = [True] * N

    m = int(N ** 0.5)
    for i in range(2, m+1):
        if sieve[i-1] == True:
            for j in range(2*i, N//2+1, i):
                sieve[j-1] = False

    primeNumbers = [i for i in range(2, N//2+1) if sieve[i-1]]

    count = 0
    answer = []
    tempN = N
    while count < len(primeNumbers):
        if tempN % primeNumbers[count] == 0:
            tempN /= primeNumbers[count]
            answer.append(primeNumbers[count])
        else:
            count += 1

    return answer if len(answer) != 0 else [N]


    
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    for i in solution(N):
        if i != 1:
            print(i)