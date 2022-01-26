import sys

def solution(N):
    fibonacci = [(1, 0), (0, 1)]

    if N == 0:
        return fibonacci[0]

    index = 2
    while index <= N:
        zero = fibonacci[index-1][0] + fibonacci[index-2][0]
        one = fibonacci[index-1][1] + fibonacci[index-2][1]
        fibonacci.append((zero, one))

        index += 1

    return fibonacci[-1]

    

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    N = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

    for i in N:
        answer = solution(i)
        print(answer[0], answer[1])
