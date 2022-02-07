import sys

def solution():
    dp = [[0] * (K+1) for _ in range(N+1)]

    #i는 아이템을 의미하고, j는 maxWeight를 의미한다.
    #즉 각 아이템 별로 무게 K까지의 최대 value를 저장하게된다.
    for i in range(1, N+1):
        for j in range(1, K+1):
            weight = things[i-1][0]
            value = things[i-1][1]

            if j < weight: #j보다 무게가 무거우면 해당 물건은 넣을 수 없다.
                dp[i][j] = dp[i-1][j] #이전 물건이 들어간 value와 같다.
            else: #j보다 무게가 가벼우면 해당 물건은 넣을 수 있다.
                # 이전 물건을 넣은 최대 value와 이전 물건에 해당 물건이 더해진 value중 큰 값을 저장하게 된다.
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

    return dp[N][K] #N개의 물건을 모두 탐색하고 무게가 K일때의 최대 value를 리턴한다.
    

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    things = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution())

