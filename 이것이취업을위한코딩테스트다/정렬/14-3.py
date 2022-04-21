#[programmers 실패율]
#---answer---#
def solution(N, stages):
    #배열들의 인덱스가 스테이지 번호가 됨
    challenge = [0 for _ in range(N+1)] # 도전자 수
    notClear = [0 for _ in range(N+1)] # 클리어 하지 못한 수

    # 주어진 사람들의 현재 스테이지를 탐색
    for i in stages:
        for j in range(1, N+1): # 전체 스테이지를 탐색
            # 현재 사람의 스테이지가 탐색중인 스테이지 번호보다 크면 도전을 한 상태
            if i > j: 
                challenge[j] += 1 # 스테이지의 도전자 수 증가

            # 현재 사람의 스테이지가 탐색중인 스테이지와 같은 경우 도전은 했지만 클리어는 못한 상태
            elif i == j: 
                challenge[j] += 1 # 스테이지의 도전자 수 증가
                notClear[j] += 1 # 스테이지의 클리어하지 못한 사람의 수 증가

    answer = [] # 실패율을 저장할 배열
    # 각 스테이지 번호를 탐색
    for i in range(1, N+1):
        # 도전자의 수가 0일 경우
        if challenge[i] == 0:
            answer.append((0, i))
        # 도전자의 수가 0이 아닐 경우 
        else:
            answer.append((notClear[i]/challenge[i], i)) # 실패율과 스테이지 번호 저장

    # 실패율을 내림차순으로 스테이지 번호를 오름차순으로 정렬
    answer = sorted(answer, key=lambda x: (-x[0], x[1]))

    return [i[1] for i in answer] # 스테이지 번호를 반환

#---solution---#
# def solution(N, stages):
#     answer = []
#     length = len(stages)

#     # 스테이지 번호를 1부터 N까지 증가시키며
#     for i in range(1, N+1):
#         # 해당 스테이지에 머물러 있는 사람의 수를 계산
#         count = stages.count(i)

#         # 실패율 계산
#         if length == 0:
#             fail = 0
#         else:
#             fail = count / length

#         # 리스트에 (스테이지 번호, 실패율) 원소 삽입
#         answer.append((i, fail))
#         length -= count

#     # 실패율을 기준으로 각 스테이지를 내림차순으로 정렬
#     answer = sorted(answer, key=lambda t: t[1], reverse=True)

#     # 정렬된 스테이지 번호를 출력
#     answer = [i[0] for i in answer]
#     return answer