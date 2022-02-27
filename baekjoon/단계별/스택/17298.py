import sys

def solution():
    stack = []
    answer = [-1] * N

    for i in range(N):
        while stack and A[stack[-1]] < A[i]:
            answer[stack.pop()] = A[i]
        stack.append(i)

    return answer


    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    A = list(map(int, sys.stdin.readline().split()))
    
    print(*solution())