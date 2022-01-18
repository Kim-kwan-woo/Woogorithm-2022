import sys

def solution(N):
    F = [0, 1]

    for i in range(2, N+1):
        F.append(F[i-2]+F[i-1])

    return F[N]
    


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    print(solution(N))