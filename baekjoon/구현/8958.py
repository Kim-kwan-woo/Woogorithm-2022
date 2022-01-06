import sys

def solution(oxList):
    score = []
    for i in oxList:
        tempScore = 0
        sumScore = 1
        for j in range(len(i)):
            if i[j] == 'O':
                tempScore += sumScore
                sumScore += 1
            else:
                sumScore = 1
        score.append(tempScore)
    
    return score

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    oxList = []
    for i in range(N):
        oxList.append(sys.stdin.readline().rstrip())
    
    for i in solution(oxList):
        print(i)