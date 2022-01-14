import sys

def solution(N):
    mulNum = 1
    for i in N:
        mulNum *= i

    countList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in str(mulNum):
        countList[int(j)] += 1

    return countList


if __name__ == "__main__":
    N = []
    for i in range(3):
        N.append(int(sys.stdin.readline().rstrip()))
    
    for i in solution(N):
        print(i)