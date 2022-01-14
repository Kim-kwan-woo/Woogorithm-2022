import sys

def solution(N):
    remainder = set([i%42 for i in N])

    return len(remainder)


if __name__ == "__main__":
    N = []
    for i in range(10):
        N.append(int(sys.stdin.readline().rstrip()))
    
    print(solution(N))