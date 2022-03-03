import sys

#---answer---
N, M = map(int, sys.stdin.readline().split())
cards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

maxCard = min(cards[0])
for i in range(1, N):
    if min(cards[i]) > maxCard:
        maxCard = min(cards[i])

print(maxCard)


#---solution---
# # N, M을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# result = 0
# #한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     #현재 줄에서 가장 작은 수 찾기
#     min_value = min(data)
#     #가장 작은 수들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)

# print(result) #최종 답안 출력