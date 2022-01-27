import sys

def solution(P):
    dp = [1, 1, 1, 2, 2]
    answer = []

    for i in P:
        if len(dp) >= i:
            answer.append(dp[i-1])
            continue

        for i in range(len(dp), i):
            dp.append(dp[i-1] + dp[i-5])
        
        answer.append(dp[-1])
    
    return answer
    
    

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    P = [int(sys.stdin.readline().rstrip()) for _ in range(T)]

    for i in solution(P):
        print(i)

