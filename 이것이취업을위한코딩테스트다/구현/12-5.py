import sys

#[baekjoon 3190]
#---answer---#
N = int(sys.stdin.readline().rstrip()) #보드의 크기
K = int(sys.stdin.readline().rstrip()) #사과의 개수
apples = [list(map(int, sys.stdin.readline().split())) for _ in range(K)] # 사과의 위치
L = int(sys.stdin.readline().rstrip()) # 방향 변환 정보 개수
commands = [list(sys.stdin.readline().split()) for _ in range(L)] #방향 변환 정보

# 게임 보드 판 그리기(테두리를 1씩 키워서 값을 2로 설정하고 실제 게임 보드 판은 값을 0으로 저장)
board = [[0 if (i != 0 and i != N+1 and j != 0 and j != N+1) else 2 for i in range(N+2)] for j in range(N+2)]

# 게임 보드판에 사과의 위치를 1로 저장
for i in apples:
    board[i[0]][i[1]] = 1

board[1][1] = 2 # 뱀의 시작 위치를 2로 설정
move = [(0, 1), (1, 0), (0, -1), (-1, 0)] #뱀이 이동하는 움직임 

time, tailTime = 0, 0 #전체시간, 꼬리가 줄어든 시간
x, y = 1, 1 # 뱀의 머리의 x,y 위치
tailX, tailY = 1, 1 # 뱀의 꼬리의 x, y 위치
moveIndex, cmdIndex = 0, 0 #머리의 움직임 인덱스와 방향 전환 인덱스
tailMoveIndex, tailCmdIndex = 0, 0 #꼬리의 움직임 인덱스와 방향 전환 인덱스

# 게임 시작
while True:
    time += 1 # 전체 시간 증가
    # 뱀의 머리 이동 좌표
    x += move[moveIndex][0]
    y += move[moveIndex][1]

    if board[x][y] == 2: # 이동한 뱀의 머리가 2를 만나면 게임판을 벗어나거나 몸통과 부딪힌 경우
        break # 게임 종료
    elif board[x][y] == 0: # 이동한 맴의 머리가 0을 만나면 꼬리를 하나 이동하여 길이를 줄인다.
        board[tailX][tailY] = 0 #꼬리를 줄인다.
        # 현재 꼬리의 위치 재 설정
        tailX += move[tailMoveIndex][0]
        tailY += move[tailMoveIndex][1]
        tailTime += 1 #꼬리가 줄어든 시간 증가
    
    board[x][y] = 2 # 머리 이동

    # 머리의 이동 시간을 방향 변환 정보와 비교하여 방향 전환
    if cmdIndex < L and time == int(commands[cmdIndex][0]): 
        if commands[cmdIndex][1] == "D": #D인 경우 오른쪽으로 90도 회전
            moveIndex = (moveIndex+1) % 4
        else: #L인 경우 왼쪽으로 90도 회전
            moveIndex = (moveIndex-1) % 4
        cmdIndex += 1 #다음 방향 변환 정보로 이동

    # 꼬리의 이동 시간을 방향 변환 정보와 비교하여 방향 전환  
    if tailCmdIndex < L and tailTime == int(commands[tailCmdIndex][0]):
        if commands[tailCmdIndex][1] == "D": #D인 경우 오른쪽으로 90도 회전
            tailMoveIndex = (tailMoveIndex+1) % 4
        else: #L인 경우 왼쪽으로 90도 회전
            tailMoveIndex = (tailMoveIndex-1) % 4
        tailCmdIndex += 1 #다음 방향 변환 정보로 이동

print(time) #게임이 종료된 시간 출력

#---solution---#
# n = int(input())
# k = int(input())
# data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
# info = [] # 방향 회전 정보

# #맵 정보(사과 있는 곳을 1로 표시)
# for _ in range(k):
#     a, b = map(int, input.split())
#     data[a][b] = 1

# #방향 회전 정보 입력
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))

# #처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == "L":
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1 #뱀의 머리 위치
#     data[x][y] = 2 #뱀이 존재하는 위치는 2로 표시
#     direction = 0 # 처음에는 동쪽을 보고 있음
#     time = 0 # 시작한 뒤에 지난 초 시간
#     index = 0 # 다음에 회전할 정보
#     q = [(x, y)] #뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
#     while True:
#         nx = x + dx[direction]
#         ny = x + dy[direction]

#         #맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             #사과가 없다면 이동 후에 꼬리 제거
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             #사과가 있다면 이동 후에 꼬리 그대로 두기
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         #벽이나 뱀의 몸통과 부딪혔다면
#         else:
#             time += 1
#             break
#         x, y = nx, ny # 다음 위치로 머리를 이동
#         time += 1
#         if index < 1 and time == info[index][0]: #회전할 시간인 경우 회전
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time

# print(simulate())