import sys

#[음료수 얼려 먹기]
#---answer---#
N, M = map(int, sys.stdin.readline().split()) #가로 세로 크기 입력
iceCube = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)] #얼음틀 입력

#얼음틀 탐색 함수
def countIcecream(x, y): 
    iceCube[x][y] = 1 # 현재 얼음 틀 위치의 값을 1로 변경

    if y-1 > 0 and iceCube[x][y-1] == 0: #좌측 위치 탐색
        countIcecream(x, y-1)
    if x-1 > 0 and iceCube[x-1][y] == 0: #위쪽 위치 탐색
        countIcecream(x-1, y)
    if y+1 < M and iceCube[x][y+1] == 0: #우측 위치 탐색
        countIcecream(x, y+1)
    if x+1 < N and iceCube[x+1][y] == 0: #아래쪽 위치 탐색
        countIcecream(x+1, y)

count = 0 #전체 아이스크림 개수
#전체 얼음틀 탐색
for i in range(N):
    for j in range(M):
        if iceCube[i][j] == 0: #0이 시작하는 위치에서 탐색 시작
            count += 1 #아이스크림 개수 증가
            countIcecream(i, j)

print(count)

#---solution---#
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# # 2치원 리스트의 맵 정보 입력받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노들들도 방문
# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         #해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# # 모든 노드(위치)에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1

# print(result) # 정답 출력