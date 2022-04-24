import sys
import heapq

#[baekjoon 1715 카드 정렬하기]
#---answer---#
N = int(sys.stdin.readline().rstrip()) # 카드 묶음 수
card = [int(sys.stdin.readline().rstrip()) for _ in range(N)] # 각 묶음의 카드의 개수
count = 0

if N == 1:
    print(count)
    exit(0)
    
heapq.heapify(card)

while True:
    
    nowCards = heapq.heappop(card) + heapq.heappop(card)
    count += nowCards

    if not card:
        print(count)
        break

    heapq.heappush(card, nowCards)

# #---solution---#
# n = int(input())

# # 힙(Heap)에 초기 카드 묶음을 삽입
# heap = []
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)

# result = 0

# # 힙(Heap)에 원소가 1개 남을 때까지
# while len(heap) != 1:
#     # 가장 작은 2개의 카드 묶음 꺼내기
#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)
#     # 카드 묶음을 합쳐서 다시 삽입
#     sum_value = one + two
#     result += sum_value
#     heapq.heappush(heap, sum_value)

# print(result)
