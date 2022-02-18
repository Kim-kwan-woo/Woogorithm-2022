import sys

sys.setrecursionlimit(3000)

def solution():
    
    dp = [[0]*(len(secondSeq)+1) for _ in range(len(firstSeq)+1)]

    for i in range(1, len(firstSeq)+1):
        for j in range(1, len(secondSeq)+1):
            if firstSeq[i-1] == secondSeq[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]
    
if __name__ == "__main__":
    firstSeq = list(sys.stdin.readline().rstrip())
    secondSeq = list(sys.stdin.readline().rstrip())
    
    print(solution())
    