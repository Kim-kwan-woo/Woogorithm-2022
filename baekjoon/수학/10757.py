import sys

def solution(A, B):
    return A+ B
    

    
if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    print(solution(A, B))