import sys

def solution(N):
    sumNum = 0
    step = 1
    while sumNum < N:
        sumNum += step
        step += 1

    if (step-1) % 2 == 0:
        return str(N-sumNum+step-1) + '/' + str(sumNum-N+1)
    else:
         return str(sumNum-N+1) + '/' + str(N-sumNum+step-1)



if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))
    