import sys

def solution(numList):
    return sorted(numList)

        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numList = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    for i in solution(numList):
        print(i)