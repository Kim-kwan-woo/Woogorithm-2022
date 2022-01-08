import sys

def solution(A, B):
    if A > B:
        return '>'
    elif A < B:
        return '<'
    else:
        return '=='
    

if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    print(solution(A, B))