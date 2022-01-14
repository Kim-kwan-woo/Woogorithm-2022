import sys

def solution(N):
    maxNum = N // 5
    for i in range(maxNum, -1, -1):
        if (N - (i * 5)) % 3 == 0:
            return i + ((N - (i * 5)) // 3)
        
    return -1
    

    
if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    print(solution(N))