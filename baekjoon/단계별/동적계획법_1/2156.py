import sys

def solution(N, wine):
    answer = [[0, wine[0]], [wine[1], (wine[0]+wine[1])]]
    for i in range(2, N):
        print(i)
        if answer[i-1][1] >= answer[i-2][1]:
            answer.append([answer[i-1][1], answer[i-2][1]+wine[i]])
        else:
            answer.append([answer[i-1]])

    return answer[-1]



        

    

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    wine = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

    print(solution(n, wine))

