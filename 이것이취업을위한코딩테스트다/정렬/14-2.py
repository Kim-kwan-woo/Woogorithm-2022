import sys

#[baekjoon 18310 안테나]
#---answer---#
N = int(sys.stdin.readline().rstrip()) # 집의 수
home = list(map(int, sys.stdin.readline().split())) # 집들의 위치

home.sort() # 집들의 위치를 오름차순으로 정렬

print(home[(N-1)//2]) # 가운데 위치한 집에 설치해야 거리의 총합이 최소가 됨

#---solution---#
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# # 중간값(median)을 출력
# print(data[(n-1) // 2])