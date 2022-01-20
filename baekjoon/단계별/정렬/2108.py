import sys

def solution(numList):
    numList = sorted(numList)
    avg = round(sum(numList)/len(numList))
    mid = numList[len(numList)//2]

    count = 0
    countList = []
    for i in range(len(numList)):
        if i == 0 or numList[i] == numList[i-1]:
            count += 1
            if i+1 == len(numList):
                countList.append((numList[i], count))
        else:
            countList.append((numList[i-1], count))
            count = 1

    countList = sorted(countList, key= lambda x : (-x[1], x[0]))

    fre = countList[0][0]
    if len(countList) != 1 and countList[0][1] == countList[1][1]:
        fre = countList[1][0]

    ran = numList[-1] - numList[0]

    return (avg, mid, fre, ran)


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numList = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    for i in solution(numList):
        print(i)