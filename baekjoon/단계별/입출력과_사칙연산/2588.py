import sys

def solution(a, b):
    return [a*int(b[2]), a*int(b[1]), a*int(b[0])  ,a*int(b)]

if __name__ == "__main__":
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    for i in solution(int(a), b):
        print(i)
