import sys

#[programmers 문자열 압축]
#---answer---#
def solution(s):
    # 문자열의 길이가 1인 경우 1리턴
    if len(s) == 1:
        return 1

    minCount = sys.maxsize # 최소 문자열을 개수를 저장할 변수

    #문자열 길이의 절반까지 자를 수 있으므로 범위를 아래와 같이 설정
    for i in range(1, (len(s)//2)+1):
        startStr = s[:i] #비교할 앞의 자른 문자열
        n, count = i, 0 #n은 현재 인덱스 count는 자르는 문자열의 길이의 최소 문자열 길이
        numCount = 1 #같은 문자열의 개수를 저장하는 변수
        #문자열의 길이를 벗어나지 않는 범위에서 탐색
        while n+i <= len(s):         
            currentStr = s[n:n+i] #비교할 뒤의 자른 문자열
            if startStr != currentStr: # 두 문자열이 다른 경우
                if numCount != 1: #앞에서 같았던 문자열의 개수가 1개보다 큰 경우
                    count += len(str(numCount)) #숫자의 길이만큼을 count에 더해준다.
                    numCount = 1 #numCount 초기화
                count += i # 앞의 문자열의 길이만큼을 count에 더한다.
                startStr = currentStr #비교할 앞의 문자열을 비교할 뒤의 문자열로 변경
            else: # 두 문자열이 같은 경우
                numCount += 1 # 같은 문자열의 개수를 저장하는 numCount를 증가 시킨다.

            n += i # 인덱스를 i만큼 이동한다.

        # 문자열의 끝까지 도달했을때 계속 문자열이 같았을 경우
        if numCount != 1:
            count += len(str(numCount)) #같았던 문자열의 길이만큼을 더해준다.
        count += len(s[n-i:]) # 뒤에 남은 문자열의 길이를 더해준다.
        minCount = min(count, minCount) # min 연산으로 최소의 문자열의 길이를 구한다.ㄴ

    return minCount

#---solution---#
# def solution(s):
#     answer = len(s)
#     #1개 단위(step)부터 압축 단위를 늘려가며 확인
#     for step in range(1, len(s) // 2 + 1):
#         compressed = ""
#         prev = s[0:step] #앞에서부터 step만큼의 문자열 추출
#         count = 1
#         # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
#         for j in range(step, len(s), step):
#             # 이전 상태와 동일하다면 압축 횟수(count)wmdrk
#             if prev == s[j:j+step]:
#                 count += 1
#             # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j+step] # 다시 상태 초기화
#                 count = 1
            
#         #남아있는 문자열에 대해 처리
#         compressed += str(count) + prev if count >= 2 else prev
#         #만들어지는 압축 문자열이 가장 짧은 것이 정답
#         answer = min(answer, len(compressed))

#     return answer