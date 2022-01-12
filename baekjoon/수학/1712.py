import sys
import math

def solution(A, B, C):
    if B >= C:
        return -1
    else: 
        return math.floor(A/(C-B)) + 1



if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(solution(A, B, C))
    
