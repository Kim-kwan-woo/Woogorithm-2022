import sys

#---answer---#
N = int(sys.stdin.readline().rstrip())
commands = list(sys.stdin.readline().split())

point = [1, 1]

for i in commands:
    if i == "R" and point[1] < (N-1):
        point[1] += 1
    elif i == "L" and point[1] > 1:
        point[1] -= 1
    elif i == "D" and point[0] < (N-1):
        point[0] += 1
    elif i == "U" and point[0] > 1:
        point[0] -= 1
    

print(*point)

#---solution---#
# # N을 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# #이동 계획을 하나씩 확인
# for plan in plans:
#     #이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     #공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     #이동 수행
#     x, y = nx, ny

# print(x, y)