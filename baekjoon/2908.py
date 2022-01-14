import sys

def solution(A, B):
    A = A[-1] + A[-2] + A[-3]
    B = B[-1] + B[-2] + B[-3]

    return max(A, B)

if __name__ == "__main__":
    A, B = sys.stdin.readline().split()
    
    print(solution(A, B))