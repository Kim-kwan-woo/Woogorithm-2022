import sys
# 재귀 함수로 구현(메모리 초과 발생)
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
def solution(N, star):
    count = 0
    while count != int(N**(1/3))-1:
        stars = []
        for i in range(len(star) * 3):
            if i // len(star) == 1:
                stars.append(star[i % len(star)] + " " * len(star) + star[i%len(star)])
            else:
                stars.append(star[i % len(star)] * 3)

        star = stars
        count += 1

    for i in star:
        print(i)
    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    star = ["***", "* *", "***"]

    solution(N, star)

