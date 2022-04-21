import sys

#[두 배열의 원소 교체]
#---answer---#
N, K = map(int,sys.stdin.readline().split()) # N = 숫자의 개수, K = 교체 횟수
A = list(map(int, sys.stdin.readline().split())) 
B = list(map(int, sys.stdin.readline().split()))

A.sort() # A배열을 오름차순으로 정렬
B.sort(reverse=True) # B배열을 내림차순으로 정렬

# 교체가 끝난 배열
resultArr = A[K:] + B[:K]

print(sum(resultArr)) # 배열의 합을 출력

#---solution---#
# n, k = map(int, input().split()) # N과 K를 입력받기
# a = list(map(int, input().split())) # 배열 A의 원소를 입력받기
# b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

# a.sort() # 배열 A는 오름차순 정렬 수행
# b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
# for i in range(k):
#     # A의 원소가 B의 원소보다 작은 경우
#     if a[i] < b[i]:
#         # 두 원소를 교체
#         a[i], b[i] = b[i], a[i]
#     else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
#         break

# print(sum(a)) # 배열 A의 모든 원소의 합을 출력
