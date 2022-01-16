import sys

def solution(point):
    x, y = 0, 0
    pointX = [i[0] for i in point]
    pointY = [i[1] for i in point]

    for i in range(len(point)):
        if pointX.count(pointX[i]) == 1:
            x = pointX[i]
        
        if pointY.count(pointY[i]) == 1:
            y = pointY[i]

    return str(x) + " " + str(y)


    
if __name__ == "__main__":
    point = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]
    print(solution(point))