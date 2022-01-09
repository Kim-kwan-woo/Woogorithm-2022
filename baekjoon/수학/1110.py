import sys

def solution(N):
    cycle = 0
    tempNum = str(N)
    while True:
        cycle += 1

        if len(tempNum) == 1:
            tempNum += tempNum
        else:
            sumNum = int(tempNum[0]) + int(tempNum[1])
            if len(str(sumNum)) == 1:
                tempNum = tempNum[1] + str(sumNum)[0]
            else:
                tempNum = tempNum[1] + str(sumNum)[1]

        if int(tempNum) == N:
            return cycle

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))