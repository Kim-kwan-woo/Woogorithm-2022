import sys

#재귀 함수로 구현(메모리 초과 발생)
# def solution(N, star, count):
#     stars = []
#     for i in range(len(star) * 3):
#         if i // len(star) == 1:
#             stars.append(star[i % len(star)] + " " * len(star) + star[i%len(star)])
#         else:
#             stars.append(star[i % len(star)] * 3)

#     if count == int(N**(1/3))-1:
#         for j in stars:
#             print(j)
#     else:  
#         solution(N, stars, count+1)

#비 재귀 함수로 구현(메모리 초과 발생)
# def solution(N, star):
#     count = 0
#     while count != int(N**(1/3))-1:
#         stars = []
#         for i in range(len(star) * 3):
#             if i // len(star) == 1:
#                 stars.append(star[i % len(star)] + " " * len(star) + star[i%len(star)])
#             else:
#                 stars.append(star[i % len(star)] * 3)

#         star = stars
#         count += 1

#     for i in star:
#         print(i)

#실행할 카운트를 메인에서 따로 계산하고 그 만큼 반복하여 함수를 실행하면 메모리 초과가 발생하지 않음
def solution(star):
    matrix = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            matrix.append(star[i%len(star)] + " " * len(star) + star[i%len(star)])
        else:
            matrix.append(star[i%len(star)]*3)
    return matrix 

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    star = ["***", "* *", "***"]

    count = 0
    while N != 3:
        N = int(N/3)
        count += 1

    for i in range(count):
        star = solution(star)
    for i in star:
        print(i)

