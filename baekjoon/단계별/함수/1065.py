import sys

def solution(num):
    if len(str(num)) == 1:
        return True

    tempList = list(map(int, str(num)))
    gap = tempList[1] - tempList[0]
    check = True
    for i in range(1, len(tempList)):
        if tempList[i] - tempList[i-1] != gap:
            check = False
            break
    
    return check

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    numList = []
    count = 0
    for i in range(1, N+1):
        if solution(i) == True:
            count += 1

    print(count)