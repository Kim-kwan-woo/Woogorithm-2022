import sys

def solution(stairs):
    if len(stairs) == 1:
        return stairs[0]
        
    answer = [[stairs[0]], [stairs[1], stairs[0]+stairs[1]]]

    for i in range(2, len(stairs)):
        answer.append([max(answer[i-2])+stairs[i], answer[i-1][0]+stairs[i]])


    return max(answer[-1])
        

    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

    print(solution(stairs))

