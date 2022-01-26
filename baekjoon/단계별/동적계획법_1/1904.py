import sys

def solution(N):
    dp = [1, 2]
    if N <= 2:
        return dp[N-1]
        
    for i in range(2, N):
        dp.append((dp[i-1] + dp[i-2]) % 15746)

    return dp[-1]
    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))

