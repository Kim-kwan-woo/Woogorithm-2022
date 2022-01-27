import sys

def solution(N):
    count = [0, 1, 1]
    
    for i in range(4, N+1):
        if i % 3 == 0 and i % 2 == 0:
            count.append(min(count[i//3-1], count[i//2-1], count[i-2])+1)
        elif i % 3 == 0:
            count.append(min(count[i//3-1], count[i-2])+1)
        elif i % 2 == 0:
            count.append(min(count[i//2-1], count[i-2])+1)
        else:
            count.append(count[i-2]+1)

    return count[N-1]
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    print(solution(N))

