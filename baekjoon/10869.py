import sys

def solution(a, b):
    return [a+b, a-b, a*b, a//b, a%b]

if __name__ == "__main__":
    a, b = map(int, sys.stdin.readline().split())
    for i in solution(a, b):
        print(i)
