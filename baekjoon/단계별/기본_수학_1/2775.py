import sys

def solution(k, n):
    apart = [[i+1 for i in range(n)] for j in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, n):
            apart[i][j] = apart[i-1][j] + apart[i][j-1]

    return apart[-1][-1]
    
    
if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        answer.append(solution(k, n))

    for i in answer:
        print(i)