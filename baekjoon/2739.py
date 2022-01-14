import sys

def solution(N):
    for i in range(1, 10):
        print(str(N) + " * " + str(i) + " = " + str(N*i))

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    solution(N)