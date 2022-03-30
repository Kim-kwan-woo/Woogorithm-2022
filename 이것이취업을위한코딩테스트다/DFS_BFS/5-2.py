import sys
from collections import deque

#[미로 탈출]
#---answer---#
N, M = map(int, sys.stdin.readline().split()) #가로 세로 크기 입력
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)] #미로 입력

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우 이동

def bfs(x, y):
    queue = deque([]) # 큐 생성
    queue.append((x, y)) # 시작 위치 큐에 저장

    while queue: #큐가 비어있을 때까지 반복
        x, y = queue.popleft() # 큐에서 맨 앞의 위치를 꺼낸다
        # 상, 하, 좌, 우 이동
        for i in range(4):
            moveX = x + move[i][0] # x 이동 위치
            moveY = y + move[i][1] # y 이동 위치

            if moveX >= 0 and moveX < N and moveY >= 0 and moveY < M: # 미로를 벗어나지 않는 경우
                if maze[moveX][moveY] == 1: # 해당 위치에 처음 이동한 경우
                    maze[moveX][moveY] = maze[x][y] + 1 # 이동한 위치의 값을 변경
                    queue.append((moveX, moveY)) # 이동한 위치를 큐에 저장

    return maze[-1][-1] # 도착 위치의 값을 반환

print(bfs(0, 0))

#---solution---#
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())
# # 2차원 리스트의 맵 정보 입력받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # 이동할 네 방향 정의(상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS 소스코드 구현
# def bfs(x, y):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때까지 반복
#     while queue:
#         x, y = queue.popleft()
#         # 현재 위치에서 네 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = x + dx[i]
#             # 미로 찾기 공간을 벗어난 경우 무시
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))

#     # 가장 오른쪽 아래까지의 최단 거리 반환
#     return graph[n - 1][m - 1]

# # BFS를 수행한 결과 출력
# print(bfs(0, 0))