#[programmers 자물쇠와 열쇠]
#---answer---#
def solution(key, lock):
    lockLen = len(lock) + 2*(len(key)-1) #확장할 자물쇠의 크기
    zeroCount = sum(lock, []).count(0) #자물쇠의 홈의 개수

    expandedLock = [[0] * lockLen for _ in range(lockLen)] #확장된 자물쇠

    #확장된 자물쇠의 가운데에 자물쇠 값 저장
    for i in range(len(key)-1, lockLen-len(key)+1):
        for j in range(len(key)-1, lockLen-len(key)+1):
            expandedLock[i][j] = lock[i-len(key)+1][j-len(key)+1]

    count,rotateCount = 0, 0 #count는 열쇠의 돌기와 자물쇠의 홈이 만나는 개수, rotateCount는 열쇠 회전 수
    #열쇠를 3번 회전할때 까지 반복
    while rotateCount != 4:
        for i in range(lockLen-len(key)+1): #확장된 자물쇠 행 탐색(key가 들어갈 수 있는 길이까지)
            for j in range(lockLen-len(key)+1): #확장된 자물쇠 열 탐색(key가 들어갈 수 있는 길이까지)
                tempCheck = True # 열쇠의 돌기와 자물쇠의 돌기가 만나는 지를 판단할 변수
                for n in range(len(key)): #열쇠 행 탐색
                    for m in range(len(key)): #열쇠 열 탐색
                        #확장된 자물쇠에서 열쇠와 자물쇠의 위치가 기존 자물쇠의 위치에 포함되는 경우에만 판별
                        if (i+n >= len(key) -1 and i+n <= lockLen-len(key)) and (j+m >= len(key) -1 and j+m <= lockLen-len(key)):
                            #열쇠의 돌기와 자물쇠의 돌기가 만나는 경우
                            if key[n][m] == 1 and expandedLock[i+n][j+m] == 1:
                                tempCheck = False #열릴 수 없다
                                break # 열릴 수 없으므로 해당 열쇠 위치 탐색 종료
                            #열쇠의 돌기와 자물쇠의 홈이 만나는 경우
                            elif key[n][m] == 1 and expandedLock[i+n][j+m] == 0:
                                count += 1 #카운트 증가

                    #열쇠의 돌기와 자물쇠의 돌기가 만나는 경우
                    if not tempCheck:
                        break #열릴 수 없으므로 해당 열쇠 위치 탐색 종료
                #열쇠를 모두 탐색했을 때 열쇠의 돌기와 자물쇠의 돌기가 만나는 부분이 없고
                #자물쇠의 홈이 모두 채워진 경우
                if tempCheck and count == zeroCount:
                    return True # true 리턴

                count = 0 #카운트 초기화

        key = rotateKey(key) #열쇠 회전
        rotateCount += 1 #열쇠 회전 횟수 증가

    #모든 경우 탐색 후 열리는 경우가 없으므로 false리턴
    return False

#열쇠를 90도 회전
def rotateKey(key):
    newKey = [[0] * len(key) for _ in range(len(key[0]))] # 회전된 열쇠

    #열쇠 회전
    for i in range(len(key[0])):
        for j in range(len(key)):
            if key[j][i] != 0:
                newKey[i][len(key)-1-j] = key[j][i]

    return newKey

#---solution---#
# # 2차원 리스트 90도 회전
# def rotate_a_matrix_by_90_degree(a):
#     n = len(a) # 행 길이 계산
#     m = len(a[0]) # 열 길이 계산
#     result = [[0] * n for _ in range(m)] # 결과 리스트
#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = a[i][j]
#     return result

# #자물쇠의 중간 부분이 모두 1인지 확인
# def check(new_lock):
#     lock_lenth = len(new_lock) // 3
#     for i in range(lock_lenth, lock_lenth*2):
#         for j in range(lock_lenth, lock_lenth * 2):
#             if new_lock[i][j] != 1:
#                 return False
    
#     return True

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     #자물쇠의 크기를 기존의 3배로 변환
#     new_lock = [[0] * (n*3) for _ in range(n*3)]
#     #새로운 자물쇠 중앙 부분에 기존의 자물쇠 넣기
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]

#     #4가지 방향에 대해서 확인
#     for rotation in range(4):
#         key = rotate_a_matrix_by_90_degree(key)# 열쇠 회전
#         for x in range(n*2):
#             for y in range(n*2):
#                 #자물쇠에 열쇠를 끼워넣기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] + key[i][j]
#                 #새로운 자물쇠에 열쇠가 정확히 들어맞나 검사
#                 if check(new_lock) == True:
#                     return True
#                 #자물쇠에서 열쇠를 다시 빼기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]

#     return False