import sys

#---answer---#
S = sys.stdin.readline().rstrip()

alphaList = [] # 알파벳들을 저장할 리스트
totalSum = 0 # 숫자들의 총합
#전체 문자열 탐색
for i in S: 
    if i.isalpha(): # 문자가 알파벳인 경우
        alphaList.append(i) # 알파벳 리스트에 삽입
    else: # 문자가 숫자인 경우
        totalSum += int(i) #총 합에 더해줌

#문자열을 연결하여 결과 생성
result = ''.join(sorted(alphaList)) + str(totalSum)
print(result)

# #---solution---#
# data = input()
# result = []
# value = 0

# #문자를 하나씩 확인하며
# for x in data:
#     #알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():
#         result.append(x)
#     #숫자는 따로 더하기
#     else:
#         value += int(x)

# #알파벳을 오름차순으로 정렬
# result.sort()

# #숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))

# #최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))


