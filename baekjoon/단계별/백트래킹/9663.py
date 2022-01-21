import sys

def solution(N, step):
    global count
    if step == N:
        count += 1
        
    else:
        for i in range(N):
            if visited[i] == False:
                chess[step] = i
                check = True

                for j in range(step):
                    if (chess[step] == chess[j]) or ((step - j) == abs(chess[step] - chess[j])):
                        check = False

                if check:
                    visited[i] = True
                    solution(N, step+1)
                    visited[i] = False
                


        

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip()) 
    count = 0
    visited = [False for _ in range(N)]
    chess = [0 for _ in range(N)]
    solution(N, 0)
    print(count)
