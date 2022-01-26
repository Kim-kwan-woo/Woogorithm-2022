import sys

def solution(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return solution(20, 20, 20)
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = solution(a, b, c-1) + solution(a, b-1, c-1) - solution(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = solution(a-1, b, c) + solution(a-1, b-1, c) + solution(a-1, b, c-1) - solution(a-1, b-1, c-1)
    return dp[a][b][c]
    

if __name__ == "__main__":
    dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
    answer = []
    while True:
        a, b, c = map(int, sys.stdin.readline().split())
        
        if a == -1 and b == -1 and c == -1:
            break
        
        answer.append((a, b, c, solution(a, b, c)))
    
    for i in answer:
        print("w({}, {}, {}) = {}".format(i[0], i[1], i[2], i[3]))
