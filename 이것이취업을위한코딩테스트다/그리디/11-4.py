import sys

#---answer---#
N = int(sys.stdin.readline().rstrip())
coins = list(map(int, sys.stdin.readline().split()))

coins.sort()

price = 1
for i in coins:
    if price < i:
        break

    price += i

print(price)

#---solution---#
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     #만들수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x

# # 만들 수 없는 금액 출력
# print(target)