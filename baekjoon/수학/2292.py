import sys

def solution(N):
    step = 1
    tempN = 1
    while N > tempN:
        tempN = tempN + (6*step)
        step += 1

    return step



if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))
    
