import sys

#[위에서 아리로]
#---answer---#
N = int(sys.stdin.readline().rstrip()) # 숫자의 개수
nums = [int(sys.stdin.readline().rstrip()) for _ in range(N)] #숫자 입력

nums.sort(reverse=True) # 내림차순으로 정렬

print(*nums) # 배열의 원소 출력

#---solution---#
# # N을 입력받기
# n = int(input())

# # N개의 정수를 입력받아 리스트에 저장
# array = []
# for i in range(n):
#     array.append(int(input()))

# # 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
# array = sorted(array, reverse=True)

# # 정렬이 수행된 결과 출력
# for i in array:
#     print(i, end=" ")
