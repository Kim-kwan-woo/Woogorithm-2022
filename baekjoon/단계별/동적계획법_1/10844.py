import sys

def solution(N):
    answer = [9, 17, 32]
    if N <= 3:
        return answer[N-1] % 1000000000 

    for i in range(3, N):
        answer.append(2*(answer[-1]-((i-2)*3)) + ((i-2)*3))

    return answer[-1] % 1000000000
        

    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    print(solution(N))

