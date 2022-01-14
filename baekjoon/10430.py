import sys

def solution(a, b, c):
    return [(a+b)%c, ((a%c) + (b%c))%c, (a*b)%c, ((a%c) * (b%c))%c]

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    for i in solution(a, b, c):
        print(i)
