import sys

def solution(K):
    count = 0
    for i in range(len(coins)-1, -1, -1):
        if coins[i] <= K:
            coinCount = K//coins[i]
            K -= coins[i]*coinCount
            count += coinCount
        
        if K == 0:
            break
        
    return count
    

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
    print(solution(K))

