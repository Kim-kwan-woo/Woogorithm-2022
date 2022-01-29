import sys

def solution(times):
    times = sorted(times, key=lambda x: (x[1], x[0]))
    meeting = times[0]
    count = 1

    for i in range(1, len(times)):
        if meeting[1] <= times[i][0]:
            meeting = times[i]
            count += 1

    return count
        


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    times =  [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(times))

