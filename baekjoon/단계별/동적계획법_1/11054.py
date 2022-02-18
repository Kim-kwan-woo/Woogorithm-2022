import sys

def solution():
    #A의 처음부터 끝까지 -1의 간격으로 접근
    reversedA = A[::-1]

    increse = [1] * N
    decrese = [1] * N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                increse[i] = max(increse[i], increse[j]+1)
            if reversedA[i] > reversedA[j]:
                decrese[i] = max(decrese[i], decrese[j]+1)

    for i in range(N):
        #증가수열과 감소수열의 기준 값은 같은 값이므로 1을 빼줘야 한다.
        increse[i] += decrese[N-i-1] - 1

    return max(increse)

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A = list(map(int, sys.stdin.readline().split()))
    
    print(solution())
    