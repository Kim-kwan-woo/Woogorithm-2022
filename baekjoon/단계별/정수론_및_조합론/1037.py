import sys

def solution(numbers):
    numbers = sorted(numbers)

    if N % 2 == 0:
        return numbers[0] * numbers[-1]
    else:
        return numbers[N//2] ** 2

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numbers = list(map(int, sys.stdin.readline().split()))

    print(solution(numbers))
    