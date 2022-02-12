import sys

def solution(n, r):
    #조합의 개수(n!/(n-r)!*r!) - n개의 원소중 서로 다른 r개를 순서없이 뽑기만 하는 경우의 수
    multi = [1]

    for i in range(1, n+1):
        multi.append(multi[i-1]*i)

    return multi[n] // (multi[n-r]*multi[r])




if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    bridge = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

    answer = []
    for i in bridge:
        answer.append(solution(i[1], i[0]))

    for i in answer:
        print(i)
    