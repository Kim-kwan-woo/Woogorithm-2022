import sys

def solution(x):
    sortedX = sorted(set(x))
    xDict = {x:i for i,x in enumerate(sortedX)}
    for i in x:
        print(xDict[i], end=' ')


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    x = list(map(int,sys.stdin.readline().split()))

    solution(x)