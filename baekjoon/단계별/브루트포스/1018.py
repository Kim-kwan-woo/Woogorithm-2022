import sys

def solution(N, M, chess):
    firstChess = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            elif i != 0 and j == 0:
                if chess[i][j] == chess[i-1][j]:
                    firstChess[i][j] = True
                    if chess[i][j] == 'W':
                        chess[i][j] = 'B'
                    else:
                        chess[i][j] = 'W'
            else:
                if chess[i][j] == chess[i][j-1]:
                    firstChess[i][j] = True
                    if chess[i][j] == 'W':
                        chess[i][j] = 'B'
                    else:
                        chess[i][j] = 'W'
    
    minCount = sys.maxsize
    for i in range(N-7):
        for j in range(M-7):
            tempList = sum([row[j:j+8] for row in firstChess[i:i+8]], [])
            
            count = tempList.count(True)
            minCount = min(minCount, count, 64-count)

    return minCount

        
    


if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    chess = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    print(solution(N, M, chess))

