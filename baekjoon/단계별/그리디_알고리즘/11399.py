import sys

def solution(times):
    times = sorted(times)
    totalTime = 0
    for i in range(1, len(times)):
        times[i] += times[i-1]

    return sum(times)
        


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    times = list(map(int, sys.stdin.readline().split()))
    print(solution(times))

