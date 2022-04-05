import sys
from collections import deque

#[baekjoon 18405 경쟁적 전염]
#---answer---#
# N - 시험관의 크기 / K - 바이러스 종류
N, K = map(int, sys.stdin.readline().split())
tube = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# S - 경과 시간 / X, Y 결과 좌표
S, X, Y = map(int, sys.stdin.readline().split())

# 각 바이러스의 종류 별로 위치를 저장할 배열
indexMap = [deque([]) for _ in range(K+1)]

# 바이러스의 종류 별로 위치 정보를 저장
for i in range(N):
    for j in range(N):
        if tube[i][j] != 0:
            indexMap[tube[i][j]].append((i, j))

# 바이러스 전파
for _ in range(S): # S 시간 만큼 반복
    # 각 바이러스 종류 별로 위치를 탐색
    for i in range(1, len(indexMap)):
        for j in range(len(indexMap[i])):
            x, y = indexMap[i].popleft() # 현재 바이러스의 위치

            if x-1 >= 0 and tube[x-1][y] == 0: # 상
                tube[x-1][y] = i
                indexMap[i].append((x-1, y))
            if x+1 < N and tube[x+1][y] == 0: # 하
                tube[x+1][y] = i
                indexMap[i].append((x+1, y))
            if y-1 >= 0 and tube[x][y-1] == 0: # 좌
                tube[x][y-1] = i
                indexMap[i].append((x, y-1))
            if y+1 < N and tube[x][y+1] == 0: # 우
                tube[x][y+1] = i
                indexMap[i].append((x, y+1))

print(tube[X-1][Y-1]) # 결과 위치의 바이러스 출력

#---solution---#
# n, k = map(int, input().split())

# graph = [] # 전체 보드 정보를 담는 리스트
# data = [] # 바이러스에 대한 정보를 담는 리스트

# for i in range(n):
#     # 보드 정보를 한 줄 단위로 입력
#     graph.append(list(map(int, input().split())))
#     for j in range(n):
#         # 해당 위치에 바이러스가 존재하는 경우
#         if graph[i][j] != 0:
#             # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
#             data.append((graph[i][j], 0, i, j))

# # 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
# data.sort()
# q = deque(data)

# target_s, target_x, target_y = map(int, input().split())

# # 바이러스가 퍼져나갈 수 있는 4가지 위치
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# # 너비 우선 탐색(BFS) 진행
# while q:
#     virus, s, x, y = q.popleft()
#     # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
#     if s == target_s:
#         break
#     # 현재 노드에서 주변 4가지 위치를 각각 확인
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 해당 위치로 이동할 수 있는 경우
#         if 0 <= nx and nx < n and 0 <= ny and ny < n:
#             # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(graph[target_x-1][target_y-1])
