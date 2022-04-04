import sys
from collections import deque

#[baekjoon 18352 특정 거리의 도시 찾기]
#---answer---#
# N - 도시의 개수 / M - 도로의 개수 / K - 거리 정보 / X - 출발 도시의 번호 
N, M, K, X = map(int, sys.stdin.readline().split())
road = [[] for _ in range(N+1)] # 도로 연결 정보를 저장할 배열

# 각 도시에 연결된 도로의 정보를 저장
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    road[start].append(end)

def bfs():
    queue = deque([(X, 0)]) # 큐 생성 (시작 위치를 저장해서)
    visited = [False] * (N+1) # 각 도시의 방문 정보를 저장
    answer = []

    visited[X] = True # 첫 시작 위치를 방문 으로 설정
    while queue: #큐가 비어있을 때까지 반복
        x, count = queue.popleft() # 큐에서 맨 앞의 위치를 꺼낸다
        if count == K: # 이동한 거리의 수가 K와 같을 때
                answer.append(x) # 현재 도시의 위치를 저장
        else: # 이동한 거리의 수가 K가 아닐 때
            for i in road[x]: # 현재 도시에 연결된 모든 도로로 이동
                if not visited[i]: # 이동하는 도시가 방문하지 않은 경우에만 이동
                    queue.append((i, count+1)) # 큐에 다음 도시 저장
                    visited[i] = True # 다음 도시의 방문 정보를 방문으로 저장
                    
    if answer: # 결과 값이 있을 경우
        return sorted(answer) # 정렬해서 리턴
    else: # 결과 값이 없을 경우
        return [-1] # -1 리턴

# 정답 출력
for i in bfs():
    print(i)

#---solution---#
# # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]

# # 모든 도로의 정보를 입력받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# # 모든 도시에 대한 최단 거리 초기화
# distance = [-1] * (n+1)
# distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# # 너비 우선 탐색(BFS) 수행
# q = deque([x])
# while q:
#     now = q.popleft()
#     #현재 도시에서 이동할 수 있는 모든 도시를 확인
#     for next_node in graph[now]:
#         # 아직 방문하지 않은 도시라면
#         if distance[next_node] == -1:
#             # 최단 거리 갱신
#             distance[next_node] = distance[now]+1
#             q.append(next_node)

# # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
# check = False
# for i in range(1, n+1):
#     if distance[i] == k:
#         print(i)
#         check = True

# # 만약 최단 거리가 K인 도시가 없다면, -1 출력
# if check == False:
#     print(-1)