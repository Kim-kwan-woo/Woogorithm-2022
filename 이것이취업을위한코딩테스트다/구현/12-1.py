import sys

#[baekjoon 18406]
#---answer---#
N = sys.stdin.readline().rstrip()

numList = list(map(int, N)) # 입력받은 숫자를 하나씩 나눠 리스트로 저장

firstSum = sum(numList[:len(numList)//2]) #처음부터 절반까지의 합
secondSum = sum(numList[len(numList)//2:]) #절반부터 끝 까지의 합

# 두 합이 같은 경우
if firstSum == secondSum:
    print("LUCKY")
# 두 합이 같지 않은 경우
else:
    print("READY")

#---solution---#
# n = input()
# length = len(n) #점수 값의 총 자릿수
# summary = 0

# #왼쪽 부분의 자릿수 합 더하기
# for i in range(length // 2):
#     summary += int(n[i])

# #오른쪽 부분의 자릿수 합 빼기
# for i in range(length // 2, length):
#     summary -= int(n[i])

# #왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
# if summary == 0:
#     print("LUCKY")
# else:
#     print("READY")
