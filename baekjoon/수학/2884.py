import sys

def solution(H, M):
    if M >= 45:
        return (H, M-45)
    else:
        return (H-1 if H > 0 else 23, 15+M)
    

if __name__ == "__main__":
    H, M = map(int, sys.stdin.readline().split())
    time = solution(H, M)
    print(time[0], time[1])