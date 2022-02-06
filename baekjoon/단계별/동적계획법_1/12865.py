import sys

#메모리 초과!!!!
def solution():
    dp = []
    maxValue = 0
    if things[0][0] <= K:
        maxValue = things[0][1]
    for i in range(N):
        for j in dp:
            if things[i][0] + j[0] <= K:
                tempList = [things[i][0] + j[0], things[i][1] + j[1]]
                if maxValue < tempList[1]:
                    maxValue = tempList[1]
                if tempList[0] < K:
                    dp.append(tempList)
        if things[i][0] < K:
            dp.append(things[i])

    return maxValue

    

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    things = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution())

