import sys

def solution(poles):
    poles = sorted(poles, key=lambda x: x[0]) #정렬
    answer = [1] * N

    # 증가하는 수열의 최대 길이
    for i in range(len(poles)):
        for j in range(i):
            if poles[i][1] > poles[j][1]:
                answer[i] = max(answer[i] , answer[j]+1)

    return N - max(answer)

    


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    poles = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(poles))

