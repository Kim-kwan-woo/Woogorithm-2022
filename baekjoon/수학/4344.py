import sys

def solution(scoreList):
    percent = []
    for i in scoreList:
        tempList = list(map(int, i.split(' ')))
        avg = sum(tempList[1:])/tempList[0]

        count = 0
        for j in range(1, tempList[0]+1):
            if tempList[j] > avg:
                count += 1
        
        percent.append(round(count/tempList[0]*100, 3))

    return percent

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    scoreList = []
    for i in range(N):
        scoreList.append(sys.stdin.readline().rstrip())
    
    for i in solution(scoreList):
        print("{:.3f}".format(i) + "%")