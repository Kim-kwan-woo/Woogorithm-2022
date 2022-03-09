import sys

#---answer---#
point = sys.stdin.readline().rstrip() #현재위치 입력받기

#ord(a) == 97    ord(h) == 104
point = [ord(point[0]), int(point[1])] #현재 위치를 숫자로 변환
move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)] #이동 가능한 경우

count = 0
#이동 가능한 경우의 수 탐색
for i in move:
    current = [point[0] + i[0], point[1] + i[1]] # 좌표 이동

    #이동된 좌표가 체스판을 벗어나는지 확인
    if (current[0] >= 97 and current[0] <= 104) and (current[1] >= 1 and current[1] <= 8):
        count += 1 # 벗어나지 않는다면 개수 증가

print(count)

#---solution---#
# #현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# #나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     #이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)