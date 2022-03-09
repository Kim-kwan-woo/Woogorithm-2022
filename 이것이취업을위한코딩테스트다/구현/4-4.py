import sys

#---answer---#
# 데이터 입력
N, M = map(int, sys.stdin.readline().split())
point = list(map(int, sys.stdin.readline().split()))
gameMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서 이동 좌표

count = 1 # 방문한 개수 카운트
rotateCount = 0 # 회전한 횟수 카운트

while True:
    # 왼쪽 방향으로 회전
    rotateCount += 1 # 회전 횟수 증가
    if point[2] - 1 != -1:
        point[2] -= 1
    else:
        point[2] = 3
    
    movePoint = [point[0] + move[point[2]][0], point[1] + move[point[2]][1]] # 이동 위치
    # 이동 위치가 맵을 벗어나지 않을 경우
    if (movePoint[0] >= 0 and movePoint[0] < N) and (movePoint[1] >= 0 and movePoint[1] < M):
        # 이동 위치가 육지인 경우
        if gameMap[movePoint[0]][movePoint[1]] == 0:
            count += 1 # 방문 개수 증가
            rotateCount = 0 # 회전 횟수 초기화
            gameMap[point[0]][point[1]] = 1 # 원래 있던 지점을 1로 변경
            point[0], point[1] = movePoint[0], movePoint[1] # 현재 위치를 이동한 위치로 변경
            continue

    # 4번 회전하는 동안 이동하지 못한 경우
    if rotateCount == 4:
        movePoint = [point[0] - move[point[2]][0], point[1] - move[point[2]][1]] # 이동 위치(뒤로 한칸)
        # 이동 위치가 맵을 벗어나지 않는 경우
        if (movePoint[0] >= 0 and movePoint[0] < N) and (movePoint[1] >= 0 and movePoint[1] < M):
            # 이동 위치가 육지인 경우
            if gameMap[movePoint[0]][movePoint[1]] == 0:
                count += 1 # 방문 개수 증가
                rotateCount = 0 # 회전 횟수 초기화
                gameMap[point[0]][point[1]] = 1 # 원래 있던 지점을 1로 변경
                point[0], point[1] = movePoint[0], movePoint[1] # 현재 위치를 이동한 위치로 변경
            else: # 최종적으로 이동하지 못하는 경우
                break
        else: # 최종적으로 이동하지 못하는 경우
            break
    
print(count)

#---solution---#
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# # 현재 캐릭터의 x좌표, y좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표를 방문 처리

# # 전체 맵 정보를 입력 받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split)))

# # 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# #왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3

# # 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#     #왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] == 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     #네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         # 뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         # 뒤가 바다로 막혀있는 경우
#         else: 
#             break
#         turn_time = 0

# #정답 출력
# print(count)