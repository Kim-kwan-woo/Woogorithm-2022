import sys

def solution(x, y, w, h):
    minX = min(x, w-x)
    minY = min(y, h-y)

    return min(minX, minY)


    
if __name__ == "__main__":
    x, y, w, h = map(int,sys.stdin.readline().split())
    print(solution(x, y, w, h))

