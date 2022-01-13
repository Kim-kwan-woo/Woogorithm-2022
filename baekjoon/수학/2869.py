import sys
import math

def solution(A, B, V):
    return math.ceil((V-A) / (A-B)) + 1
    

    
if __name__ == "__main__":
    A, B, V = map(int, sys.stdin.readline().split())
    print(solution(A, B, V))