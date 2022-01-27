import sys

def solution(houses):
    RGB = houses[0]
    for i in range(1, len(houses)):
        houses[i][0] += min(houses[i-1][1], houses[i-1][2]) #R
        houses[i][1] += min(houses[i-1][0], houses[i-1][2]) #G
        houses[i][2] += min(houses[i-1][0], houses[i-1][1]) #B

    return min(houses[-1])
    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(houses))

