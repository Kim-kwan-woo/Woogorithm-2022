import sys

def solution(points):
    return sorted(points, key= lambda x: (x[0], x[1]))


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    for i in solution(points):
        print(i[0], i[1])