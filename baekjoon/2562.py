import sys

def solution(N):
    maxNum = N[0]
    maxIndex = 0
    for i, num in enumerate(N):
        if num > maxNum:
            maxNum = num
            maxIndex = i
    return [maxNum, maxIndex+1]

if __name__ == "__main__":
    N = []
    for i in range(9):
        N.append(int(sys.stdin.readline().rstrip()))

    answer = solution(N)
    print(answer[0])
    print(answer[1])
