import sys

def solution(listN):
    return [min(listN), max(listN)]

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    listN = list(map(int, sys.stdin.readline().split()))

    print(solution(listN)[0], solution(listN)[1])
