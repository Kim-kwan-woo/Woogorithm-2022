#[programmers 괄호 변환]
#---answer---#
def solution(p):
    answer = "" # 결과 문자열 
    openCount, closeCount = 0, 0 # 열린 괄호의 수, 닫힌 괄호의 수
    u, v = "", "" 
    
    # 입력 받은 문자열이 "" 이면 리턴
    if p == "":
        return ""
    
    #u, v 나누기
    for i in range(len(p)):
        if p[i] == "(":
            openCount += 1
        else:
            closeCount += 1
            
        if openCount == closeCount:
            u = p[:i+1]
            v = p[i+1:]
            break
                        
        
    # u가 올바른 괄호 문자열인 경우
    if u[-1] == ")":
        u += solution(v)
        return u
    
    # u가 올바른 괄호 문자열이 아닌 경우
    answer += "(" + solution(v) + ")"
    u = list(u[1:-1]) # 문자열의 맨 앞과 맨 뒤를 자름
    # 문자열의 모든 괄호를 반대로 전환
    for i in range(len(u)):
        if u[i] == "(":
            u[i] = ")"
        else:
            u[i] = "("
                
    answer += ''.join(u)
        
    return answer # 결과 반환

#---solution---#
# # 균형잡힌 괄호 문자열의 인덱스 반환
# def balanced_index(p):
#     count = 0 # 왼쪽 괄호의 개수
#     for i in range(len(p)):
#         if p[i] == '(':
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             return i

# # 올바른 괄호 문자열인지 판단
# def check_proper(p):
#     count = 0 # 왼쪽 괄호의 개수
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0: # 쌍이 맞지 않는 경우에 False 반환
#                 return False
#             count -= 1
#     return True # 쌍이 맞는 경우에 True 반환

# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
#     index = balanced_index(p)
#     u = p[:index + 1]
#     v = p[index + 1:]
#     # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
#     if check_proper(u):
#         answer = u + solution(v)
#     # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#         answer += "".join(u)
#     return answer