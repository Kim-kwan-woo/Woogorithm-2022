import sys

def solution(a, b):
    return a-b

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    print(solution(a, b))
