import sys
from itertools import combinations

#[baekjoon 15686]
#---answer---#
N, M = map(int, sys.stdin.readline().split()) #N = 도시 크기, M=최대 유지 치킨집 수

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #도시의 정보 입력

house = [] #집의 좌표를 저장할 배열
chicken = [] #치킨집의 좌표를 저장할 배열

#도시를 탐색하며 집과 치킨집의 좌표를 각각 배열에 저장
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i+1, j+1])
        elif city[i][j] == 2:
            chicken.append([i+1, j+1])

answer = [] #유지되는 치킨집의 경우에 따라 최소의 치킨 거리를 저장할 배열

# M개의 치킨집을 선택하는 경우를 모두 탐색
for i in combinations(chicken, M):
    totalDistance = 0 # 최소인 도시의 치킨 거리를 저장할 변수
    #모든 집을 탐색
    for j in house: 
        minDistance = sys.maxsize #현재 집에서 최소인 치킨 거리를 저장할 변수
        for k in range(M): #선택된 치킨 집 중 최소인 거리를 계산
            distance = abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]) #치킨 거리 계산
            # 현재 집에서의 최소 치킨 거리인지 확인
            if distance < minDistance:
                minDistance = distance

        totalDistance += minDistance # 도시의 치킨 거리에 현재 집의 치킨 거리를 더한다.

    answer.append(totalDistance) #선택된 치킨집의 경우의 최소 도시 치킨거리를 배열에 저장

#배열에 저장된 값들 중 최소 도시 치킨거리를 출력
print(min(answer))

#---solution---#
# n, m = map(int, input().split())
# chicken, house = [], []

# for r in range(n):
#     data = list(map(int, input().split()))
#     for c in range(n):
#         if data[c] == 1:
#             house.append((r, c)) # 일반 집
#         elif data[c] == 2:
#             chicken.append((r, c)) # 치킨 집

# # 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
# candidates = list(combinations(chicken, m))

# #치킨 거리의 합을 계산하는 함수
# def get_sum(candidate):
#     result = 0
#     #모든 집에 대하여
#     for hx, hy in house:
#         #가장 가까운 치킨집을 찾기
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx-cx) + abs(hy-cy))
#         #가장 가까운 치킨집까지의 거리를 더하기
#         result += temp
#     #치킨 거리의 합 반환

# #치킨 거리의 합의 최소를 찾아 출력
# result = 1e9
# for candidate in candidates:
#     result = min(result, get_sum(candidate))

# print(result)