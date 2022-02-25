import sys

def solution():
    index = 0
    stack = []
    while index != N:
        for i in range(index+1, N):
            if A[index] < A[i]:
                stack.append(A[i])
                break
        
        if len(stack) != index+1:
            stack.append(-1)
        
        index += 1

    return stack
    
    

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    A = list(map(int, sys.stdin.readline().split()))
    
    print(*solution())