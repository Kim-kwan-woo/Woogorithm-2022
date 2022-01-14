import sys
import math

def solution(H, W, N):
    room = math.ceil(N/H)
    floor = N % H

    if len(str(room)) == 1:
        room = '0' + str(room)
    
    if floor == 0:
        floor = H
        
    return str(floor) + str(room)
    

    
if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    answer = []
    for i in range(T):
        H, W, N = map(int, sys.stdin.readline().split())
        answer.append(solution(H, W, N))

    for i in answer:
        print(i)