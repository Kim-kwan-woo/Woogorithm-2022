import sys
from itertools import combinations

#[baekjoon 15686]
#---answer---#
N, M = map(int, sys.stdin.readline().split())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i+1, j+1])
        elif city[i][j] == 2:
            chicken.append([i+1, j+1])

answer = []
for i in combinations(chicken, M):
    totalDistance = 0
    for j in house:
        minDistance = sys.maxsize
        for k in range(M):
            distance = abs(j[0] - i[k][0]) + abs(j[1] - i[k][1])
            if distance < minDistance:
                minDistance = distance

        totalDistance += minDistance

    answer.append(totalDistance)

print(min(answer))