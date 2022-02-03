import sys

def solution(N, wine):
    if N == 1:
        return wine[0]

    answer = [[0, wine[0]], [wine[1], (wine[0]+wine[1])]]
    maxNum = wine[0]
    for i in range(2, N):
        answer.append([maxNum + wine[i], answer[i-1][0] + wine[i]])
        if max(answer[i-1]) > maxNum:
            maxNum = max(answer[i-1])

    return max(sum(answer, []))



        

    

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    wine = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    print(solution(n, wine))

