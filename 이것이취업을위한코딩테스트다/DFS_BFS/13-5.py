import sys

#[baekjoon 14888 연산자 끼워 넣기]
#---answer---#
N = int(sys.stdin.readline().rstrip()) # 수의 개수
nums = list(map(int,sys.stdin.readline().split())) # 연산을 할 숫자들
operators = list(map(int,sys.stdin.readline().split())) # 연산자 개수 정보

answer = []

def solution(num, index):
    # 숫자의 위치가 마지막 숫자라면
    if index == len(nums):
        answer.append(num) # 결과를 저장
    else:
        # 4가지 연산에 대해 수행
        for j in range(4):
            if operators[j] != 0:
                operators[j] -= 1
                if j == 0: #더하기
                    solution(num+nums[index], index+1)
                elif j == 1: #빼기
                    solution(num-nums[index], index+1)
                elif j == 2: #곱하기
                    solution(num*nums[index], index+1)
                else: #나누기
                    if num < 0:
                        solution(-(abs(num)//nums[index]), index+1)
                    else:
                        solution(num//nums[index], index+1)
                operators[j] += 1 # 연산 후에 연산자의 개수를 원래대로 복구
        

solution(nums[0], 1) # 모든 연산을 수행
print(max(answer)) # 최댓값 출력
print(min(answer)) # 최솟값 출력

#---solution---#
# n = int(input())
# # 연산을 수행하고자 하는 수 리스트
# data = list(map(int, input().split()))
# # 더하기, 빼기, 곱하기, 나누기 연산자 개수
# add, sub, mul, div = map(int, input().split())

# # 최솟값과 최댓값 초기화
# min_value = 1e9
# max_value = -1e9

# # 깊이 우선 탐색(DFS) 매서드
# def dfs(i, now):
#     global min_value, max_value, add, sub, mul, div
#     # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
#     if i == n:
#         min_value = min(min_value, now)
#         max_value = max(max_value, now)
#     else:
#         # 각 연산자에 대하여 재귀적으로 수행
#         if add > 0:
#             add -= 1
#             dfs(i+1, now + data[i])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             dfs(i+1, now - data[i])
#             sub += 1
#         if mul > 0:
#             mul -= 1
#             dfs(i+1, now * data[i])
#             mul += 1
#         if div > 0:
#             div -= 1
#             dfs(i+1, int(now / data[i])) # 나눌 때는 나머지를 제거
#             div += 1

# # DFS 메서드 호출
# dfs(1, data[0])

# # 최댓값과 최솟값 차례대로 출력
# print(max_value)
# print(min_value)