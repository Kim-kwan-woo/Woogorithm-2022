import sys

def solution(A, B):
    return A+B

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    N = []
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        N.append(solution(A,B))
    
    for i in N:
        print(i)